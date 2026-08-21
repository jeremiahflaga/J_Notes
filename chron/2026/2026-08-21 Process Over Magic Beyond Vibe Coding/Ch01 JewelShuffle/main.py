"""
Jewel Shuffle - a cute, mouse-only match-3 game made with pygame.

How to play:
    Click a jewel, then click a neighboring jewel to swap them.
    Match 3 or more jewels of the same kind in a row or column to pop them!
    Chain reactions score bonus points.

Run with:
    pip install -r requirements.txt
    python main.py
"""

import math
import random
import sys

import pygame

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
GRID_SIZE = 8
CELL = 64
MARGIN = 28
TOP_BAR = 110
BOTTOM_BAR = 46

BOARD_X = MARGIN
BOARD_Y = TOP_BAR
WIDTH = CELL * GRID_SIZE + MARGIN * 2
HEIGHT = TOP_BAR + CELL * GRID_SIZE + MARGIN + BOTTOM_BAR
FPS = 60

SWAP_DURATION = 0.18
CLEAR_DURATION = 0.22
FALL_DURATION = 0.28

NUM_TYPES = 6

# Pastel, "cute" color palette
BG_TOP = (255, 240, 245)
BG_BOTTOM = (232, 232, 250)
BOARD_LIGHT = (255, 250, 240)
BOARD_DARK = (245, 233, 248)
TEXT_COLOR = (110, 80, 120)
SELECT_COLOR = (255, 210, 90)

JEWEL_COLORS = [
    (255, 133, 162),   # bubblegum pink
    (255, 176, 89),    # peach orange
    (255, 224, 102),   # buttercup yellow
    (130, 212, 250),   # sky blue
    (140, 210, 150),   # mint green
    (196, 158, 224),   # lavender purple
]


def clamp(value, low, high):
    return max(low, min(high, value))


def ease_out_cubic(t):
    t = clamp(t, 0.0, 1.0)
    return 1 - (1 - t) ** 3


def lerp(a, b, t):
    return a + (b - a) * t


# ----------------------------------------------------------------------------
# Jewel drawing (pre-rendered onto small surfaces for speed & cuteness)
# ----------------------------------------------------------------------------
def build_jewel_surface(color):
    size = CELL
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    cx, cy = size // 2, size // 2
    radius = int(size * 0.38)

    dark = tuple(max(0, c - 60) for c in color)
    light = tuple(min(255, c + 55) for c in color)

    # soft drop shadow
    pygame.draw.circle(surf, (0, 0, 0, 35), (cx + 3, cy + 5), radius)
    # main body
    pygame.draw.circle(surf, color, (cx, cy), radius)
    pygame.draw.circle(surf, dark, (cx, cy), radius, 3)
    # glossy highlight
    highlight_rect = pygame.Rect(0, 0, int(radius * 1.1), int(radius * 0.7))
    highlight_rect.center = (cx - radius * 0.32, cy - radius * 0.38)
    hl_surf = pygame.Surface(highlight_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(hl_surf, (*light, 160), hl_surf.get_rect())
    surf.blit(hl_surf, highlight_rect.topleft)

    # cute face: eyes
    eye_dx = radius * 0.34
    eye_dy = -radius * 0.05
    eye_r = max(2, int(radius * 0.14))
    for sign in (-1, 1):
        ex, ey = cx + sign * eye_dx, cy + eye_dy
        pygame.draw.circle(surf, (70, 50, 60), (int(ex), int(ey)), eye_r)
        pygame.draw.circle(surf, (255, 255, 255), (int(ex - eye_r * 0.35), int(ey - eye_r * 0.35)), max(1, eye_r // 3))

    # smile
    smile_rect = pygame.Rect(0, 0, int(radius * 0.9), int(radius * 0.8))
    smile_rect.center = (cx, cy + radius * 0.18)
    pygame.draw.arc(surf, (70, 50, 60), smile_rect, math.radians(20), math.radians(160), 2)

    # tiny blush
    blush_r = max(1, int(radius * 0.13))
    blush_dx = radius * 0.62
    for sign in (-1, 1):
        bx, by = cx + sign * blush_dx, cy + radius * 0.12
        blush_surf = pygame.Surface((blush_r * 2, blush_r * 2), pygame.SRCALPHA)
        pygame.draw.circle(blush_surf, (255, 120, 140, 90), (blush_r, blush_r), blush_r)
        surf.blit(blush_surf, (bx - blush_r, by - blush_r))

    return surf


# ----------------------------------------------------------------------------
# Board logic
# ----------------------------------------------------------------------------
def find_matches(board):
    """Return a set of (row, col) cells that are part of a run of 3+."""
    matched = set()

    def scan(length, get):
        start = 0
        for i in range(1, length + 1):
            if i < length and get(i) == get(start) and get(start) != -1:
                continue
            if i - start >= 3:
                for k in range(start, i):
                    yield k
            start = i

    for r in range(GRID_SIZE):
        for c in scan(GRID_SIZE, lambda i, r=r: board[r][i]):
            matched.add((r, c))
    for c in range(GRID_SIZE):
        for r in scan(GRID_SIZE, lambda i, c=c: board[i][c]):
            matched.add((r, c))
    return matched


def board_has_moves(board):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            for dr, dc in ((0, 1), (1, 0)):
                r2, c2 = r + dr, c + dc
                if r2 < GRID_SIZE and c2 < GRID_SIZE:
                    board[r][c], board[r2][c2] = board[r2][c2], board[r][c]
                    found = bool(find_matches(board))
                    board[r][c], board[r2][c2] = board[r2][c2], board[r][c]
                    if found:
                        return True
    return False


def generate_board():
    while True:
        board = [[random.randrange(NUM_TYPES) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        # resolve any accidental starting matches
        guard = 0
        while True:
            matches = find_matches(board)
            if not matches:
                break
            for (r, c) in matches:
                board[r][c] = random.randrange(NUM_TYPES)
            guard += 1
            if guard > 200:
                break
        if board_has_moves(board):
            return board


def is_adjacent(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def cell_center(r, c):
    return (BOARD_X + c * CELL + CELL // 2, BOARD_Y + r * CELL + CELL // 2)


def pixel_to_cell(pos):
    x, y = pos
    if not (BOARD_X <= x < BOARD_X + CELL * GRID_SIZE and BOARD_Y <= y < BOARD_Y + CELL * GRID_SIZE):
        return None
    c = (x - BOARD_X) // CELL
    r = (y - BOARD_Y) // CELL
    return (r, c)


# ----------------------------------------------------------------------------
# Sparkle particles for a little extra cuteness
# ----------------------------------------------------------------------------
class Particle:
    def __init__(self, pos, color):
        angle = random.uniform(0, math.tau)
        speed = random.uniform(40, 110)
        self.pos = [pos[0], pos[1]]
        self.vel = [math.cos(angle) * speed, math.sin(angle) * speed]
        self.life = random.uniform(0.35, 0.6)
        self.max_life = self.life
        self.color = color
        self.radius = random.uniform(2, 4)

    def update(self, dt):
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt
        self.vel[0] *= 0.9
        self.vel[1] *= 0.9
        self.life -= dt
        return self.life > 0

    def draw(self, surface):
        t = clamp(self.life / self.max_life, 0, 1)
        alpha = int(255 * t)
        r = max(1, int(self.radius * t + 1))
        s = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha), (r, r), r)
        surface.blit(s, (self.pos[0] - r, self.pos[1] - r))


# ----------------------------------------------------------------------------
# Main game
# ----------------------------------------------------------------------------
class Game:
    def __init__(self):
        self.board = generate_board()
        self.state = "idle"
        self.selected = None
        self.swap_pair = None
        self.swap_progress = 0.0
        self.clear_cells = set()
        self.clear_progress = 0.0
        self.fall_offsets = {}
        self.fall_progress = 0.0
        self.score = 0
        self.combo = 0
        self.message = ""
        self.message_timer = 0.0
        self.time = 0.0

    # -- input -------------------------------------------------------------
    def handle_click(self, pos):
        if self.state != "idle":
            return
        cell = pixel_to_cell(pos)
        if cell is None:
            return
        if self.selected is None:
            self.selected = cell
        elif cell == self.selected:
            self.selected = None
        elif is_adjacent(cell, self.selected):
            a, b = self.selected, cell
            self.selected = None
            self.start_swap(a, b, reverting=False)
        else:
            self.selected = cell

    # -- state transitions ---------------------------------------------------
    def start_swap(self, a, b, reverting):
        self.board[a[0]][a[1]], self.board[b[0]][b[1]] = self.board[b[0]][b[1]], self.board[a[0]][a[1]]
        self.swap_pair = (a, b)
        self.swap_progress = 0.0
        self.state = "swap_back" if reverting else "swap_forward"

    def start_clear(self, matched):
        self.clear_cells = matched
        self.clear_progress = 0.0
        self.state = "clear"

    def start_fall(self):
        offsets = {}
        for c in range(GRID_SIZE):
            existing = []
            existing_rows = []
            for r in range(GRID_SIZE):
                if self.board[r][c] != -1:
                    existing.append(self.board[r][c])
                    existing_rows.append(r)
            empty_count = GRID_SIZE - len(existing)
            new_types = [random.randrange(NUM_TYPES) for _ in range(empty_count)]
            new_column = new_types + existing
            new_orig_rows = [row - empty_count for row in range(empty_count)] + existing_rows
            for row in range(GRID_SIZE):
                self.board[row][c] = new_column[row]
                orig_row = new_orig_rows[row]
                drop = (row - orig_row) * CELL
                if drop > 0:
                    offsets[(row, c)] = drop
        self.fall_offsets = offsets
        self.fall_progress = 0.0
        self.state = "fall"

    def show_message(self, text, seconds=1.4):
        self.message = text
        self.message_timer = seconds

    # -- update ---------------------------------------------------------------
    def update(self, dt, particles):
        self.time += dt
        if self.message_timer > 0:
            self.message_timer -= dt

        if self.state in ("swap_forward", "swap_back"):
            self.swap_progress += dt / SWAP_DURATION
            if self.swap_progress >= 1.0:
                a, b = self.swap_pair
                if self.state == "swap_forward":
                    matched = find_matches(self.board)
                    if matched:
                        self.combo = 1
                        self.start_clear(matched)
                    else:
                        self.start_swap(a, b, reverting=True)
                else:
                    self.state = "idle"

        elif self.state == "clear":
            self.clear_progress += dt / CLEAR_DURATION
            if self.clear_progress >= 1.0:
                gained = len(self.clear_cells) * 10 * self.combo
                self.score += gained
                for (r, c) in self.clear_cells:
                    color = JEWEL_COLORS[self.board[r][c] % len(JEWEL_COLORS)]
                    center = cell_center(r, c)
                    for _ in range(6):
                        particles.append(Particle(center, color))
                    self.board[r][c] = -1
                self.clear_cells = set()
                self.start_fall()

        elif self.state == "fall":
            self.fall_progress += dt / FALL_DURATION
            if self.fall_progress >= 1.0:
                self.fall_offsets = {}
                matched = find_matches(self.board)
                if matched:
                    self.combo += 1
                    self.start_clear(matched)
                else:
                    self.combo = 0
                    if not board_has_moves(self.board):
                        self.board = generate_board()
                        self.show_message("No moves left - shuffling!")
                    self.state = "idle"

    # -- drawing ----------------------------------------------------------
    def draw_background(self, surface):
        for y in range(HEIGHT):
            t = y / HEIGHT
            color = tuple(int(lerp(BG_TOP[i], BG_BOTTOM[i], t)) for i in range(3))
            pygame.draw.line(surface, color, (0, y), (WIDTH, y))

    def draw_board_tiles(self, surface):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                rect = pygame.Rect(BOARD_X + c * CELL, BOARD_Y + r * CELL, CELL, CELL)
                color = BOARD_LIGHT if (r + c) % 2 == 0 else BOARD_DARK
                pygame.draw.rect(surface, color, rect, border_radius=10)

    def draw_jewel(self, surface, jewel_surfaces, jtype, center, scale=1.0, alpha=255):
        base = jewel_surfaces[jtype % len(jewel_surfaces)]
        if scale != 1.0:
            size = max(1, int(CELL * scale))
            img = pygame.transform.smoothscale(base, (size, size))
        else:
            img = base
        if alpha != 255:
            img = img.copy()
            img.set_alpha(alpha)
        rect = img.get_rect(center=center)
        surface.blit(img, rect)

    def draw(self, surface, jewel_surfaces, font_title, font_score, font_msg):
        self.draw_background(surface)

        # title bar
        title_surf = font_title.render("Jewel Shuffle", True, TEXT_COLOR)
        surface.blit(title_surf, title_surf.get_rect(midtop=(WIDTH // 2, 12)))
        score_surf = font_score.render(f"Score: {self.score}", True, TEXT_COLOR)
        surface.blit(score_surf, (MARGIN, 62))

        self.draw_board_tiles(surface)

        swapping_cells = set()
        if self.state in ("swap_forward", "swap_back") and self.swap_pair:
            swapping_cells = set(self.swap_pair)

        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if (r, c) in swapping_cells:
                    continue
                jtype = self.board[r][c]
                if jtype == -1:
                    continue
                center = list(cell_center(r, c))
                scale = 1.0
                alpha = 255
                if (r, c) in self.clear_cells:
                    t = ease_out_cubic(self.clear_progress)
                    scale = max(0.01, 1.0 - t)
                    alpha = int(255 * (1 - t))
                elif (r, c) in self.fall_offsets:
                    drop = self.fall_offsets[(r, c)]
                    t = ease_out_cubic(self.fall_progress)
                    center[1] -= drop * (1 - t)
                self.draw_jewel(surface, jewel_surfaces, jtype, center, scale, alpha)

        # animated swap pair drawn on top
        if swapping_cells:
            a, b = self.swap_pair
            t = ease_out_cubic(self.swap_progress)
            pos_a, pos_b = cell_center(*a), cell_center(*b)
            type_a, type_b = self.board[a[0]][a[1]], self.board[b[0]][b[1]]
            # jewel now logically at 'a' visually came from 'b', and vice versa
            center_a = (lerp(pos_b[0], pos_a[0], t), lerp(pos_b[1], pos_a[1], t))
            center_b = (lerp(pos_a[0], pos_b[0], t), lerp(pos_a[1], pos_b[1], t))
            self.draw_jewel(surface, jewel_surfaces, type_a, center_a)
            self.draw_jewel(surface, jewel_surfaces, type_b, center_b)

        # selection highlight
        if self.selected is not None:
            r, c = self.selected
            rect = pygame.Rect(BOARD_X + c * CELL, BOARD_Y + r * CELL, CELL, CELL)
            pulse = 3 + int(2 * math.sin(self.time * 6))
            pygame.draw.rect(surface, SELECT_COLOR, rect.inflate(-6, -6), width=4 + pulse // 2, border_radius=14)

        # bottom instructions / messages
        if self.message_timer > 0:
            msg_surf = font_msg.render(self.message, True, (200, 70, 90))
        else:
            msg_surf = font_msg.render("Click two jewels next to each other to swap them", True, TEXT_COLOR)
        surface.blit(msg_surf, msg_surf.get_rect(midbottom=(WIDTH // 2, HEIGHT - 12)))


def main():
    pygame.init()
    pygame.display.set_caption("Jewel Shuffle")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    try:
        font_title = pygame.font.SysFont("Comic Sans MS", 36, bold=True)
        font_score = pygame.font.SysFont("Comic Sans MS", 22, bold=True)
        font_msg = pygame.font.SysFont("Comic Sans MS", 18)
    except Exception:
        font_title = pygame.font.SysFont(None, 40)
        font_score = pygame.font.SysFont(None, 26)
        font_msg = pygame.font.SysFont(None, 20)

    jewel_surfaces = [build_jewel_surface(color) for color in JEWEL_COLORS]

    game = Game()
    particles = []

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    game = Game()
                    particles = []
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game.handle_click(event.pos)

        game.update(dt, particles)
        particles = [p for p in particles if p.update(dt)]

        game.draw(screen, jewel_surfaces, font_title, font_score, font_msg)
        for p in particles:
            p.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

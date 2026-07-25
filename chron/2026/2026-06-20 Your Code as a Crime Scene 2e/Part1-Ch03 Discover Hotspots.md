---
v-1.0.0: 2026-07-23 | 
---

# CHAPTER 3: Discover Hotspots: Create an Offender Profile of Code

this first pass through the intersection of people and code is more
detailed than in later chapters


## Mine the Evolution of Code

``` terminal
prompt> git log --numstat
```

This command outputs a detailed log of all commits


### Create a Git Log for Code Maat

```
prompt> git log --all --numstat --date=short \
--pretty=format:'--%h--%ad--%aN' --no-renames \
--after=2021-08-01 > git_log.txt
```

### Inspect Commit Activity

```
# remember to replace `maat` with the actual command,
# e.g. java -jar code-maat-1.0.4-standalone.jar
prompt> maat -l git_log.txt -c git2 -a summary

statistic, value
number-of-commits, 773
number-of-entities, 1651
number-of-authors, 107
```

### Analyze Impact: Calculating Change Frequencies of Code

The next step is to analyze the distribution of changes across the files in the
React codebase. You do that by specifying the revisions analysis:

```
prompt> maat -l git_log.txt -c git2 -a revisions

entity,n-revs
packages/react-reconciler/src/ReactFiberCommitWork.old.js, 72
packages/react-reconciler/src/ReactFiberCommitWork.new.js, 71
packages/react-reconciler/src/ReactFiberWorkLoop.new.js, 65
packages/react-reconciler/src/ReactFiberWorkLoop.old.js, 64
packages/react-reconciler/src/ReactFiberBeginWork.old.js, 60
...
```


## Explore the Complexity Dimension

The data collected so far reveals the spatial movements of programmers
within the codebase. This is the behavioral perspective, and as we discussed
in Chapter 2, Treat Your Code as a Crime Scene, on page 11, we now have
to combine it with a complexity dimension. Adding a complexity view lets you
quickly separate problematic code from areas that often change but are in
good shape.

### Get Complexity by Lines of Code

cyclomatic complexity

Halstead’s complexity measures

Cognitive Complexity

Given that existing metrics fare equally well (or badly, depending on how generous
we feel), we can aim for true simplicity: let’s use lines of code as a proxy for
code complexity.

Later in the book, we’ll turn to language-specific techniques for more
sophisticated insights. For now, let’s stick with lines of code as a reasonable
proxy for complexity.

### Count Lines with cloc

```
prompt> cloc ./ --unix --by-file --csv --quiet \
--report-file=react_complexity.csv
```


## Intersect Complexity and Effort

At this point, you have two different views of the codebase: one that reveals
the code complexity and one that shows change frequencies. We find potential
hotspots where the two views intersect

Merging the two views is straightforward ... 
I have prepared a Python script that relieves you of writing that tedious
code yourself. Grab a copy of merge_comp_freqs.py from GitHub

```
prompt> python merge_comp_freqs.py react_revisions.csv react_complexity.csv

module,revisions,code
packages/react-reconciler/src/ReactFiberCommitWork.old.js, 72, 3302
packages/react-reconciler/src/ReactFiberCommitWork.new.js, 71, 3302
packages/react-reconciler/src/ReactFiberWorkLoop.new.js, 65, 2408
packages/react-reconciler/src/ReactFiberWorkLoop.old.js, 64, 2408
packages/react-reconciler/src/ReactFiberBeginWork.old.js, 60, 3220
packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js, 43, 4369
packages/shared/ReactFeatureFlags.js, 42, 56
...
```


## Drive Refactoring via a Probability Surface

### Know Why You Don’t Have to Fix All Technical Debt

keep in mind that hotspots send a **positive message**

This preceding figure might be the **most important data point in this book**.
 - (see page 30)
 - or 6. https://tiny.one/react-change-distro

Over the past decade, I
have analyzed over 300 codebases of all sizes, scales, and domains. Every
single one of them exhibited a power law distribution. It seems to be how
software evolves, which spells good news for us. (To read more on the subject,
check out Michael Feathers’s pioneering article on “The Active Set of Classes,”
which offers an additional perspective.7)

7. https://tinyurl.com/feathers-active-set-of-classes

A power law evolution means that we don’t have to fix all technical debt, nor
should we.

**Right now, we are at the book’s central idea, and you know how to identify hotspots yourself.**

(NOTE: JBOY: I have to stop here for now)
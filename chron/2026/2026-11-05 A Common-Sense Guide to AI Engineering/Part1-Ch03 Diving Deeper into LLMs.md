---
v-1.0.0: 2026-11-08 | 
---

# CHAPTER 3: Diving Deeper into LLMs

## Diving into Tokens

... In actuality, the
LLM doesn’t generate the next **word**. Rather, it generates the next **token**.


## Diving into Embeddings

Each token of the LLM’s vocabulary is converted into what’s known as an
**embedding** (or **embedding vector**), an array of numbers that represent that token. So, the token dog might convert to an embedding of five numbers, such as [4.4, 1.9, 8.6, 0.7, 2.3]. Each individual number (such as 4.4) is called a **weight** (or **parameter**).

If, alternatively, each token was converted into 10,000
**parameters**, we’d say that our embeddings contain 10,000 **dimensions**.

When we look inside the LLM, we’ll see a giant matrix.

tokens that have similar weights at the
same dimensions may have some sort of relationship with each other

The weights are calculated based on the training data.

The weights are calculated based on the training data. As the LLM is
fed more and more data, it sees how often each token appears in the context
of other tokens and continually adjusts each token’s weights accordingly.

**inference**



## Diving into Fine-Tuning

supervised fine-tuning (SFT),
reinforcement learning (RL), and direct preference optimization (DPO)

The initial training of an LLM (based on the Internet and such) is called the
**pre-training**. The fine-tuning we do afterwards with handpicked high-quality
data is called the **post-training**.





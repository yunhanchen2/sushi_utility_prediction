## Problem Description

We are given $n$ sushi items: $\[n] = \{0, 1, 2, \dots, n - 1\}$  
Each user has a preference list: $l = (l_1, ..., l_n)$, where $l_i \in [n]$, and there will be $n$ items in each $l$.  
Our goal is to select a subset $S \subseteq [n]$, with $|S| \leq k$, to maximize the following objective:  

**Expected coverage over users:**

$$
\max_{S \subseteq [n],\ |S| \leq k} \ \mathbb{E}_{l} [ r(l, S) ]
$$

where  
$r(l, S) = 1$ if $\{l_1, ..., l_n\} \cap S \neq \emptyset$,  
and $r(l, S) = 0$ otherwise.

*(p.s. Here we use the data of `sushi_a`, which containing data id only from 0–9 and n = 10.)*


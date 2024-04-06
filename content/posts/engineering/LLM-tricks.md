---
title: 'LLM Tricks'
date: 2024-03-08T10:45:33+08:00
lastmod: 2024-03-08T10:45:33+08:00 
draft: false
tags: 
---



*   简单问题直接问，把要求写在开头或者结束。 https://arxiv.org/abs/2307.03172
    (研究发现简单问题step by step或者COT适得其反)

*   复杂问题，按照思维跳数把问题用\n分解或者用伪代码形式描述，同样重点尽量放句子两边。
    (研究发现“When separating reasoning steps, newline \n symbol works better than step i, period . or semicolon ;”)

*   找灵感头脑风暴，可以让几个AI互相扮演比如模拟审稿人和作者一问一答。

    *   e.g. 

        如果你是这篇文章的审稿人，你对作者提出哪些问题?你会为这篇文章写怎样的评语?

        If you were a reviewer for this article, what questions would you ask the author, and what would you write about this article?

        你是这篇文章的作者审稿人给你的文章review如下，请写一篇rebuttal回复审稿人提出的问题，为自己尽可能争取分数

        You are the author of this article and the reviewer gives you a review of the article below, please write a rebuttal reply to the questions asked by the reviewer and get as many points as possible for yourself

## References

*   Weng, Lilian. (Mar 2023). Prompt Engineering. Lil’Log. https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/.


*   Weng, Lilian. (Jun 2023). LLM-powered Autonomous Agents". Lil’Log. https://lilianweng.github.io/posts/2023-06-23-agent/.

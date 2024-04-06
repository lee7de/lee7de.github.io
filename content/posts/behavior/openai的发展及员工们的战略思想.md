---
title: 'openAI的发展及员工们的战略思想'
date: 2024-03-06T11:34:19+08:00
lastmod: 2024-03-06T11:34:19+08:00 
draft: false
tags: 
---

openAI的官网有许多可以学习的内容，通过研究感兴趣的内容，提高自己的思维素养和能力水平。持续更新此篇文章。

# 认识openAI

*   [2015公司情况](https://openai.com/blog/introducing-openai)

    *   OpenAI 的研究总监是世界机器学习专家之一 Ilya Sutskever。我们的 CTO 是 Greg Brockman，他是 Stripe 的前任 CTO。该小组的其他创始成员都是世界级的研究工程师和科学家：Trevor Blackwell、Vicki Cheung、Andrej Karpathy、Durk Kingma、John Schulman、Pamela Vagata 和 Wojciech Zaremba。 Pieter Abbeel、Yoshua Bengio、Alan Kay、Sergey Levine 和 Vishal Sikka 是该小组的顾问。 OpenAI 的联合主席是 Sam Altman 和 Elon Musk。

        >   OpenAI’s research director is [Ilya Sutskever](http://www.cs.toronto.edu/~ilya/), one of the world experts in machine learning. Our CTO is [Greg Brockman](https://twitter.com/gdb), formerly the CTO of Stripe. The group’s other founding members are world-class research engineers and scientists: [Trevor Blackwell](http://www.trevorblackwell.com/#), [Vicki Cheung](https://vickicheung.com/), [Andrej Karpathy](http://cs.stanford.edu/people/karpathy/), [Durk Kingma](http://dpkingma.com/), [John Schulman](http://www.eecs.berkeley.edu/~joschu/), [Pamela Vagata](https://www.linkedin.com/in/pamela-vagata-8396074), and [Wojciech Zaremba](http://cs.nyu.edu/~zaremba/). Pieter Abbeel, Yoshua Bengio, Alan Kay, Sergey Levine, and Vishal Sikka are advisors to the group. OpenAI’s co-chairs are Sam Altman and Elon Musk.

*   公司愿景 Looking forward 

    *   如今的人工智能系统拥有令人印象深刻但范围有限的功能，看来我们会不断削弱它们的限制，在极端情况下，它们几乎在每项智力任务上都将达到人类的表现。很难想象人类水平的人工智能会给社会带来多大的好处，同样也很难想象如果构建或使用不当，它会对社会造成多大的损害。

        >   AI systems today have impressive but narrow capabilities. It seems that we’ll keep whittling away at their constraints, and in the extreme case they will reach human performance on virtually every intellectual task. It’s hard to fathom how much human-level AI could benefit society, and it’s equally hard to imagine how much it could damage society if built or used incorrectly.

    *   OpenAI 是一家非营利性人工智能研究公司。我们的目标是以最有可能造福全人类的方式推进数字智能，不受产生财务回报的需求的限制。由于我们的研究没有财务义务，因此我们可以更好地关注对人类的积极影响

        >   OpenAI is a non-profit artificial intelligence research company. Our goal is to advance digital intelligence in the way that is most likely to benefit humanity as a whole, unconstrained by a need to generate financial return. Since our research is free from financial obligations, we can better focus on a positive human impact.

# Ilya Sutskever 的观点看法

*   关于openai开放技术的思考

    *   目前的技术发展到一个非常探索、不可控的阶段，如果都开源了，可能会让一些不道德的人轻松地使用大量硬件来构建不安全的人工智能，这对人工智能、人类社会的发展不好，我们可能会发展得更艰难。所以随着我们越来越接近构建人工智能，逐步减少开源是有意义的。虽然 openAI 开源可以让每个人从 AI 产品中受益，但从大局观出发，是可以选择不分享科学成果的（对于在短期和中期内的考虑，出于招聘目的，开源分享也绝对是正确的策略）。

        >   The article is concerned with a hard takeoff scenario: if a hard takeoff occurs, and a safe AI is harder to build than an unsafe one, then by opensorucing everything, we make it easy for someone unscrupulous with access to overwhelming amount of hardware to build an unsafe AI, which will experience a hard takeoff.
        >
        >   As we get closer to building AI, it will make sense to start being less open. The Open in openAI means that everyone should benefit from the fruits of AI after its built, but it's totally OK to not share the science (even though sharing everything is definitely the right strategy in the short and possibly medium term for recruitment purposes).

*   关于未来比较重要的问题方向：

    *   检测世界上是否有人正在使用秘密的突破性人工智能系统。随着分配给人工智能研究的组织和资源数量的增加，组织实现未公开的人工智能突破并将该系统用于潜在恶意目的的可能性也会增加。检测到这一点似乎很重要。我们可以想象很多方法来做到这一点——查看新闻、金融市场、在线游戏等。

        >   **Detect if someone is using a covert breakthrough AI system in the world.** As the number of organizations and resources allocated to AI research increases, the probability increases that an organization will make an undisclosed AI breakthrough and use the system for potentially malicious ends. It seems important to detect this. We can imagine a lot of ways to do this—looking at the news, financial markets, online games, etc.

    *   建立一个代理来赢得在线编程比赛。出于显而易见的原因，可以编写其他程序的程序将非常强大。

        >   **Build an agent to win online programming competitions.** A program that can write other programs would be, for obvious reasons, very powerful.

    *   网络安全防御。人工智能的早期用途是侵入计算机系统。我们希望人工智能技术能够抵御大量使用人工智能方法的复杂黑客。

        >   **Cyber-security defense.** An early use of AI will be to break into computer systems. We’d like AI techniques to defend against sophisticated hackers making heavy use of AI methods.

    *   具有许多长期生存人工智能代理的复杂模拟系统。我们有兴趣构建一个非常大的模拟，其中包含许多不同的代理，这些代理可以彼此交互、长期学习、发现语言并实现丰富多样的目标。

        **A complex simulation with many long-lived agents.** We’re interested in building a very large simulation with lots of different agents in it that can interact with each other, learn over a long period of time, discover language, and accomplish a rich variety of goals.

# Lilian Weng：The power of continuous learning 持续学习的力量

一个访谈：https://openai.com/blog/the-power-of-continuous-learning

*   Q：您如何将您的个人经验和价值观应用到您每天在 OpenAI 所做的工作中？
    How do you apply your personal experiences and values into the work you do each day at OpenAI? 

    *   A：我相信学习的力量，学习永远不会太晚。维护我的个人博客是保持这种好奇心并定期了解深度学习社区新进展的好方法。我还鼓励我的团队继续学习，无论是否与他们当前的项目相关。不同主题或领域的想法往往可以激发新的想法并拓宽潜在的解决方案空间。

        >   I believe in the power of learning and it is never too late to learn. Maintaining my personal blog is a good way to keep this curiosity going and learn about new progress in the deep learning community regularly. I also encourage my team to keep on learning, whether related or unrelated to their current projects. Ideas in different topics or fields can often inspire new ideas and broaden the potential solution space.

    *   我也坚信团队合作。如果每个人都发挥出自己最好的实力，我们就会得到1+1>2。同时，我们可能会经常遇到“脏”的工作，我个人非常愿意承担这些任务，因为只要那是最大的障碍或该任务可以为项目增加最大价值，任何事情都不应该被视为“肮脏”或“琐碎”。我鼓励我周围的人也这样做，成为团队合作者并共同努力提高团队生产力。

        >   I’m also a strong believer in teamwork. If everyone shines in their best strength, we will get 1+1 > 2. Meanwhile, we might often run into “dirty” work and personally I’m very willing to take on those tasks, because as long as that’s the biggest blocker or that task can add the biggest value into the project, nothing should be considered “dirty” or “trivial.” I encourage people around me to do the same, being a team player and working together to expedite the team productivity.

*   Q：Tell us about your blog! Why did you start it? What do you hope it inspires? 

    A：这一切都始于一套个人学习笔记。我并没有很早就进入深度学习领域，仍然认为自己是一个“新手”。最初，当我开始深入研究这么多论文时，我对不是设计算法来解决问题，而是训练模型来学习算法来解决问题的概念感到惊讶。我读得越多，我就越好奇。实际上，组织我读过的所有论文和学到的新概念变得非常困难。所以我决定开一个博客来记录和整理我的学习笔记。我也相信学习某样东西的最好方法是确保你能正确、清晰地向别人传授知识。写作帮助我到达那里。

    >   原文：It all starts as a set of personal learning notes. I didn’t enter the deep learning field super early and still considered myself a “newbie.” Initially as I started digging into so many papers, I was amazed by the concept of not designing an algorithm to solve a problem, but training a model to learn the algorithm to solve a problem. The more I read the more curious I become. Practically it became so difficult to organize all the papers I’ve read and new concepts I’ve learned. So I decided to start a blog to document and organize my learning notes. I also believe that the best way to learn something is to make sure you can teach others the knowledge correctly and clearly. Writing helps me get there.

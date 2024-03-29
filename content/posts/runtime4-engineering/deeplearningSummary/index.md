---
title: 'Deep Learning Summary'
date: 2024-02-28T10:41:23+08:00
lastmod: 2024-02-28T10:41:23+08:00 #更新时间
draft: false
---

本文的形成，特别感谢李沐老师的动手学深度学习课程、LUG主题分享中庄思源学长的深度学习分享以及众多互联网文章。

* 当人们谈论**A**rtificial **I**ntelligence（人工智能）时，其实说的是**M**achine **L**earning（机器学习），而目前的**M**achine **L**earning，主要做的是**D**eep Learning（深度学习）；Deep Learning 做的主要内容是训练Neural Networks（神经网络），训练 `Nerual Networks`其实就是在拟合函数。而确实相当多的任务可以表示函数拟合。
* 从函数拟合角度看，深度学习理论上可以用足够的数据训练足够大的感知机做预测。实际上，很难让感知机收敛到模拟各种任务，我们需要精心设计各种结构来更好地认识现实世界中的数据，比如图像用卷积、序列数据用RNN以及注意力机制等
* 深度学习也可以理解为一门编程语言，编写构造者对这个世界的理解

# 当下经典的深度学习工作流

目前深度学习应用典型的工作流包括数据、模型训练、模型部署这三方面。

## 数据Data

- Collecting, cleaning, labeling
- Data storage
- 不正确的假设：Covariate/concept/label偏移/IID以外的数据（时序、图）
- 多模块数据
- 一些例子
  - 数据采集硬件
  - 数据采集质量
  - 机器协助数据标注
  - 数据标注系统（如何管理标注员和标注质量，如何自动分配标注任务）
  - 数据质量的判断
  - 数据清洗的分布式系统（动态调度）
  - 数据存储（数据接口，压缩，备份，数据更新，某些特殊数据（比如明星的图片））

## 模型训练 Training

- Model selection, hyper-parameter tuning
  - AutoML
- Distributed training
- Preprocessing
- Monitoring
- Debugging、模型验证、模型融合
- Visualization
- 一些例子
  - 大规模分布式训练
  - 各种自动调参
  - 训练过程的监控和调试
  - 数据增强框架（特殊的噪声，特定的场景（车牌等））
  - 可视化和解释结果
  - 如何在第三方平台（比如云计算）中进行计算而不泄漏敏感数据
  - 如何充分利用专用硬件
  - 如何降低能耗

## 模型部署 Serving

- Online serving、Offline serving
  - 模型蒸馏
- Third-party platform
- 一些例子
  - 线上平台如何和现有web框架结合
  - 如何部署在线下设备，特别是算力不足的情况，比如手机等
  - 如何保证公开的模型不泄露训练数据等敏感内容
  - 如何处理对抗样本
  - 模型可解释吗？能够充分信任吗？

# The Rise of Full Stack Bottlenecks in AI applications（当下AI全栈的瓶颈）

* Deployment concerns

  * robustness to adversarial influences
  * privacy and security, especially sensitive data
  * interpretability
  * fairness
* Cost

  - Training cost
  - Labeling cost
  - Serving cost
* Accessibility

  - usable by developers and organizations without PhD-level machine learning and systems expertise

# 人工智能系统 Systems for AI（深度学习系统）

* Software systems

  - Interface, programming language
  - Metrics for models, architectures and systems
  - Tools for monitoring, interpretation, debugging, adaptation, tuning and maintenance of production AI application.
* Hardware Systems

  - Specialized hardware for certain tasks
  - Hardware using trade-offs with respect to precision, stability, fidelity, and more
  - Hardware supports distributed training/serving
* Intersection of hardware/software

  * power, latency, memory limits
  * full-stack security & privacy
  * accessibility

# 深度学习理论基础、经典内容

数学理论有：

* 线性代数：矩阵乘法
* 概率论与数理统计：统计学
* 微积分：求导
* 信息论：信息熵，度量信息损失

深度学习经典内容：

* 卷积神经网络、计算机视觉
* 循环神经网络、自然语言处理、注意力机制

![image-20240228105459443](deeplearningSummary.assets/image-20240228105459443.png)

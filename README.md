# 11PLAN

## Table of Contents

- [Computer Science Basics](## Computer Science Basics)
- [学习资源](## 学习的资源)
- [项目创意](## 项目创意)
- [自然语言处理与社交软件](## 自然语言处理与社交软件)
- [文献与研究前沿](## 文献与研究前沿 )


## 知其所以然

+ KMP算法的本质在于消除回溯，至于如何消除回溯却并不是那么难以推导的
+ Tarjan算法其实只是从后序遍历经过两个优化调整而来的
+ 排序的本质

## Computer Science Basics

### 算法复杂度分析

  - [x] 什么是时间复杂度与空间复杂度？
  - [x] 如何化简复杂度(Drop the constant and drop non dominant terms)
  - [x] 如何分析嵌套结构的复杂度？(加法原则vs乘法原则)
  - [x] 什么是摊销时间(amortized time)？
  - [x] 什么情况下会出现LogN运行时间？
  - [x] 怎么分析递归算法的运行时间，有个可以现成应用的结论是什么？

### [Internet101](https://www.khanacademy.org/computing/computer-science/internet-intro)
  - [x] What is IP and DNS(Domain Name System)? 篡改DNS指向的IP Address
  - [x] Packet, routers and reliability(***How information transform from one machine to another?*** analogy: Car traffic in rush hours)
     + A packet of information,routers
     + **TCP**(Transmission Control Protocol): 检查是不是所有的packets of information都到齐了 vs **UDP**
  - [x] HTTP and HTML[(当你在Chrome中输入google.com)的时候发生了些什么?](https://www.khanacademy.org/computing/computer-science/internet-intro/internet-works-intro/v/the-internet-http-and-html)
     + **HTTP methods such as Get/Post Request**
     + HTTPS(SSL,COOKIE and SESSION)
     + **Request and Response Circle**
  - [x] Asymmetry Encryption
  - [x] Cybersecurity and crime
     + Viruses
     + DDOS
     + Phishing(钓鱼网站)

### Must Have Knowledge on Data Structure

+ #### Arrays

+ [ ] [数组的基本概念](https://www.coursera.org/learn/data-structures/lecture/OsBSF/arrays)

  + **Contiguous area of memory** consisting of **equal-size elements** indexed by **contiguous integers**
  + Constant time access

+ [ ] 数组的基础知识

+ #### Trees

+ #### Graphs

+ #### Stacks

+ #### Queues

+ #### Heaps

+ #### Vectors

+ #### [Hash Tables](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)

  - [ ] [Implement the hash table with an array of linked list and hash code function with an Constant time O(1)](https://github.com/chenxu10/cs-study/blob/master/Implementing_Dictionary.ipynb)
  - [ ] Implement the hash table with balanced binary tree

### Must Have Knowledge on Algorithm

#### 排序

- [ ] 排序算法的稳定性
- [ ] 快排为什么那样快？
- [ ] 实现各种排序？
- [ ] 每种排序的最好、最坏和平均复杂度分别是什么场景？
- [ ] [桶排序(bucket sorting)](https://www.youtube.com/watch?v=VuXbEb5ywrU)


#### One-pass Algorithm vs Two-pass Algorithm

- [ ] Example problems solvable by one-pass algorithms
- [ ] Example problems not-solvable by one-pass algorithms

### 计算理论

+ [什么是P问题？NP问题？NPC问题？](http://www.matrix67.com/blog/archives/105)

## 学习资源

### 书籍

- [x] [Polya: How to Solve it?](https://math.berkeley.edu/~gmelvin/polya.pdf) 
- [ ] Cracking the coding interview
- [ ] Algorithm Solution Manual

### 公开课

- [ ] Berkeley CS61B
- [ ] Udacity CS101
- [ ] Princeton Algorithms One

## 项目创意

- [ ] Poem.AI(NLP+Recommendation System)
- [ ] Automate Social Media Selection(Facial Recognition+NLP)
- [ ] 自然语言服务机器人

## 自然语言处理与社交软件

## 文献与研究前沿
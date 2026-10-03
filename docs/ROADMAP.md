# 学习地图：Python → 算法 → LeetCode

目标不是“刷题数”，而是能够识别题型、解释解法，并独立写出可靠代码。按顺序推进；每阶段完成约 70% 的建议题即可进入下一阶段，同时持续复习旧题。

| 阶段 | 周数 | Python 能力 | 算法主题 | 达成标志 |
| --- | --- | --- | --- | --- |
| 0. 起步 | 第 1 周 | 变量、条件、循环、函数、list/dict/set、字符串 | 复杂度、数组、哈希表 | 能解释 `O(n)`，完成 8–10 道简单题 |
| 1. 基础结构 | 第 2–3 周 | 模块、类型标注、测试、异常 | 双指针、滑动窗口、栈、队列、链表 | 能区分双指针与滑动窗口，累计 25 题 |
| 2. 核心模式 | 第 4–6 周 | 递归、类、调试 | 二分、树、回溯、堆 | 看题能初步归类，累计 50 题 |
| 3. 进阶思维 | 第 7–10 周 | 代码重构、标准库 | 图、贪心、动态规划 | 能写出状态定义与转移，累计 80 题 |
| 4. 巩固 | 持续 | 项目化组织、复盘 | 混合题型与面试模拟 | 每周复习 10 题，累计 120 题 |

## 题型路线（建议顺序）

```text
Python 基础
  └─ 数组 / 字符串 / 哈希表
       ├─ 双指针 → 滑动窗口
       ├─ 栈 / 队列 → 链表
       └─ 二分查找
            ├─ 树（DFS / BFS）→ 回溯
            └─ 堆 → 图
                   └─ 贪心 → 动态规划
```

## 每个主题的练习清单

### 阶段 0：数组、字符串、哈希表

- 1. Two Sum
- 217. Contains Duplicate
- 242. Valid Anagram
- 49. Group Anagrams
- 238. Product of Array Except Self
- 36. Valid Sudoku
- 128. Longest Consecutive Sequence
- 125. Valid Palindrome
- 20. Valid Parentheses
- 121. Best Time to Buy and Sell Stock

### 阶段 1：双指针、滑动窗口、栈、链表

- 167. Two Sum II
- 3. Longest Substring Without Repeating Characters
- 424. Longest Repeating Character Replacement
- 239. Sliding Window Maximum
- 155. Min Stack
- 150. Evaluate Reverse Polish Notation
- 206. Reverse Linked List
- 21. Merge Two Sorted Lists
- 141. Linked List Cycle
- 19. Remove Nth Node From End of List

### 阶段 2 以后

使用 NeetCode 150 或 LeetCode Top Interview 150，仍按“主题优先”完成，而不是随机刷题。

## 复习节奏

每题标记为：`A`（独立完成）、`B`（提示后完成）、`C`（看答案后完成）。

- 当天：写解法与测试。
- 第 2 天：不看答案重写一次。
- 第 7 天：口述思路并再写关键部分。
- 第 30 天：随机抽查，只有 A 才算真正掌握。

## 卡题规则

1. 先用 5 分钟复述题目、写两个样例。
2. 独立思考 20 分钟；没有方向时只看“题型提示”。
3. 再思考 15 分钟；仍无解才看题解，并在 24 小时内闭卷重写。
4. 绝不只复制答案：必须写测试、复杂度和自己的解释。

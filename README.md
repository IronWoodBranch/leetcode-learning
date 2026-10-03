# Python × LeetCode 学习仓库

从今天开始，把每一道题都变成可运行、可测试、可复盘的练习记录。

## 快速开始

在 PowerShell 中运行：

```powershell
cd E:\Coding\LeetCode
.\.venv\Scripts\Activate.ps1
pytest
ruff check .
```

如果 PowerShell 阻止激活虚拟环境，只对当前用户执行一次：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 每次刷题流程

1. 从 [docs/ROADMAP.md](docs/ROADMAP.md) 选择当天主题和题目。
2. 运行 `python scripts/new_problem.py <分类> <题目短名>` 创建文件。
3. 先独立思考 20 分钟；再写出暴力解和优化解的思路。
4. 补充至少 3 个测试（普通、边界、重复/特殊情况），运行 `pytest`。
5. 将关键思路、时间/空间复杂度、踩坑记录写进题目文件的注释。
6. 提交一次清晰的 Git commit，例如：`solve: add two sum hash map solution`。

## 目录说明

```text
solutions/      按主题存放 LeetCode 解答
tests/          与解答对应的 pytest 测试
docs/           学习地图、每周计划与复盘规则
scripts/        创建新题目的小工具
```

今天先执行 [docs/STUDY_PLAN.md](docs/STUDY_PLAN.md) 的 Day 1；不要求速度，要求完成复盘。

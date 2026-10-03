"""LeetCode 1: Two Sum.

Idea: while scanning the array, remember each number's index.  For the current
number `value`, the required partner is `target - value`.  If that partner was
seen before, we have the answer.

Time: O(n).  Space: O(n).
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for index, value in enumerate(nums):
            partner = target - value
            if partner in seen:
                return [seen[partner], index]
            seen[value] = index

        return []

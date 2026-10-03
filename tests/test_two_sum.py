from solutions.arrays.two_sum import Solution


def test_finds_two_different_values() -> None:
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_handles_duplicate_values() -> None:
    assert Solution().twoSum([3, 3], 6) == [0, 1]


def test_returns_empty_list_when_no_pair_exists() -> None:
    assert Solution().twoSum([1, 2, 3], 10) == []

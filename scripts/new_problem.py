"""Create a starter solution and test file for a new problem.

Example:
    python scripts/new_problem.py arrays contains_duplicate
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python scripts/new_problem.py <topic> <problem_name>")

    topic, problem_name = sys.argv[1], sys.argv[2]
    if not topic.replace("_", "").replace("-", "").isalnum():
        raise SystemExit(
            "Topic must contain letters, numbers, underscores, or hyphens."
        )
    if not problem_name.replace("_", "").replace("-", "").isalnum():
        raise SystemExit(
            "Problem name must contain letters, numbers, underscores, or hyphens."
        )

    topic_path = ROOT / "solutions" / topic
    solution_path = topic_path / f"{problem_name}.py"
    test_path = ROOT / "tests" / f"test_{problem_name}.py"

    topic_path.mkdir(parents=True, exist_ok=True)
    (topic_path / "__init__.py").touch(exist_ok=True)

    if solution_path.exists() or test_path.exists():
        raise SystemExit("A solution or test with this name already exists.")

    solution_text = f"""\"\"\"LeetCode: {problem_name.replace("_", " ").title()}.\n
Idea:
Time: O(?)
Space: O(?)
\"\"\"


class Solution:
    pass
"""
    test_text = (
        f"from solutions.{topic}.{problem_name} import Solution\n\n\n"
        "def test_example() -> None:\n"
        "    solution = Solution()\n"
        "    # Arrange, act, and assert here.\n"
        "    assert solution is not None\n"
    )
    solution_path.write_text(solution_text, encoding="utf-8")
    test_path.write_text(test_text, encoding="utf-8")
    created = f"{solution_path.relative_to(ROOT)} and {test_path.relative_to(ROOT)}"
    print(f"Created {created}")


if __name__ == "__main__":
    main()

from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    for i, el in enumerate(li):
        for j, el2 in enumerate(li):
            if target == el + el2:
                return (i, j)
# Time complexity: O(n^2)
# Space complexity: O(1)


assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}, "The function didn't return the expected output."


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    prev_map = {}  # Maps each element to its index
    for i, num in enumerate(li):
        num2 = target - num
        if num2 in prev_map:
            return (prev_map[num2], i)
        prev_map[num] = i
    return prev_map
# Time complexity: O(n)
# Space complexity: O(n)


assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}, "The function didn't return the expected output."
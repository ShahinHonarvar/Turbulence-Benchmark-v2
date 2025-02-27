from typing import List

def composite_nums_between_indices(nums: List[int]) -> set:
    """
    Returns the set of all composite numbers in the given list `nums` that are between
    index 68 and index 86, both inclusive. If no composite number exists in the specified
    range, returns an empty set.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 68 and i <= 86:
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums
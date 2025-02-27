from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -81.
    """
    result = []
    start = 0
    end = 0
    prod = 1
    while end < len(nums):
        prod *= nums[end]
        while prod > -81:
            prod /= nums[start]
            start += 1
        if prod == -81:
            result.append(nums[start:end + 1])
        end += 1
    return result
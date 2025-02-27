from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -87. If no such sublist exists, returns an empty list.
    """
    result = []
    start = 0
    end = 0
    product = 1
    while end < len(nums):
        product *= nums[end]
        while product == -87:
            result.append(nums[start:end + 1])
            product /= nums[start]
            start += 1
        end += 1
    return result
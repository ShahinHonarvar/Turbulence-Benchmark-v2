from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -75. If no such sublist exists, returns an empty list.
    """
    result = []
    n = len(nums)
    for i in range(n):
        window_product = 1
        j = i
        while window_product != -75 and j < i + n:
            window_product *= nums[j % n]
            if window_product == -75:
                result.append(nums[i:j % n + 1])
            j += 1
    return result
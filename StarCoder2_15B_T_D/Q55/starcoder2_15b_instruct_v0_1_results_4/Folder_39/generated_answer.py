from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -46.
    """
    n = len(nums)
    result = []
    for i in range(n):
        window_size = 1
        while window_size <= n:
            for j in range(n):
                prod = 1
                for k in range(j, j + window_size):
                    prod *= nums[k % n]
                if prod == -46:
                    result.append([nums[(j + k) % n] for k in range(window_size)])
            window_size += 1
    return result
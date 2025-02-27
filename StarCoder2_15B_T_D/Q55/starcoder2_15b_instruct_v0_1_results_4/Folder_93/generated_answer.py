from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -91.
    """
    result = []
    n = len(nums)
    for i in range(n):
        window = []
        product = 1
        for j in range(i, i + n):
            index = j % n
            window.append(nums[index])
            product *= nums[index]
            if product == -91:
                result.append(window[:])
            if product == 0:
                break
    return result
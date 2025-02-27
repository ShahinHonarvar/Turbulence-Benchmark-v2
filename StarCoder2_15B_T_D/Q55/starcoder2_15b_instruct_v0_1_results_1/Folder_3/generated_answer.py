from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Finds all contiguous sublists in a circular list whose product equals -22.
    """
    result = []
    n = len(nums)
    for start in range(n):
        prod = 1
        for i in range(start, start + n):
            prod *= nums[i % n]
            if prod == -22:
                result.append(nums[start:i % n + 1])
                break
    return result
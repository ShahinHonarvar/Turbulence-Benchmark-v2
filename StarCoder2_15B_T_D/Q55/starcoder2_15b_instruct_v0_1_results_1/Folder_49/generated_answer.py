from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Finds all sublists of `nums` that have a product equal to -61.
    """
    result = []
    n = len(nums)
    for i in range(n):
        window = [nums[i]]
        prod = nums[i]
        j = (i + 1) % n
        while prod != -61 and j != i:
            window.append(nums[j])
            prod *= nums[j]
            j = (j + 1) % n
        if prod == -61:
            result.append(window)
    return result
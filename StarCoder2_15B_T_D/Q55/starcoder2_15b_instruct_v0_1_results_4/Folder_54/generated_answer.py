from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists of `nums` such that the product of the integers in each sublist is equal to -17.
    """
    sublists = []
    n = len(nums)
    for i in range(n):
        for j in range(i, i + n):
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -17:
                sublists.append(sublist)
    return sublists
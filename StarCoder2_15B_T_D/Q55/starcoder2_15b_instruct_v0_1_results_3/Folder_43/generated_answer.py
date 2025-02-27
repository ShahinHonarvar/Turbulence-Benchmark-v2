from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists of `nums` such that the product of the integers in each sublist is equal to -26.
    """
    result = []
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, i + len(nums)):
            index = j % len(nums)
            product *= nums[index]
            sublist.append(nums[index])
            if product == -26:
                result.append(sublist)
            elif product == 0:
                break
    return result
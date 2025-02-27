from typing import List
    from the given list such that their product equals 33.

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers
    """
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 33:
                result.append(sublist)
    return result
from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -81. Each sublist in the returned list can be of any size as long
    as it is smaller than or equal to the size of the given list. If no such sublist exists, the function
    should return an empty list. If there are duplicates of such a sublist, they should all be contained
    in the returned list. The order of sublists in the returned list does not matter.
    """
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -81:
                result.append(sublist)
    return result
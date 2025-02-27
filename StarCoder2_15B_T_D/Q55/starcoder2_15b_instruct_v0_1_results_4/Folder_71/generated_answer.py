from typing import List

def lists_with_product_equal_n(nums: List[int], n: int) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals `n`. Each sublist in the returned list can be of any size as long
    as it is smaller than or equal to the size of the given list. If no such sublist exists, the
    function returns an empty list. If there are duplicates of such a sublist, they should all be
    contained in the returned list. The order of sublists in the returned list does not matter.
    """
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if len(sublist) <= len(nums) and prod(sublist) == n:
                result.append(sublist)
    return result

def prod(nums: List[int]) -> int:
    """Returns the product of all elements in `nums`."""
    result = 1
    for num in nums:
        result *= num
    return result
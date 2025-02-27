from typing import List
import math

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Finds all sublists of the given list such that their product equals -32.
    """
    sublists = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if math.prod(sublist) == -32:
                sublists.append(sublist)
    return sublists
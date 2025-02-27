from typing import List

def lists_with_product_equal_n(nums: List[int], n: int) -> List[List[int]]:
    """
    Finds all sublists of `nums` such that their product is equal to `n`.
    """
    sublists = []
    for i in range(len(nums)):
        curr_product = 1
        curr_sublist = []
        for j in range(i, len(nums)):
            curr_product *= nums[j]
            curr_sublist.append(nums[j])
            if curr_product == n:
                sublists.append(curr_sublist[:])
            if curr_product > n:
                break
    return sublists
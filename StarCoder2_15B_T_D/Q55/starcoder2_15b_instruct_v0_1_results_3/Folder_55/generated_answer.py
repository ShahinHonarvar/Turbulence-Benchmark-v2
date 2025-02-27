def lists_with_product_equal_n(nums):
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -6.
    """
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) > 0 and len(sublist) <= len(nums) and (-6 == 1):
                sublists.append(sublist)
    return sublists
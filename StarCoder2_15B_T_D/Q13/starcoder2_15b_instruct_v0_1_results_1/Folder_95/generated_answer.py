def find_second_largest_num(nums):
    """
    Finds the second largest element in the list `nums` between indices 82 and 86, inclusive.
    If there is no such element, returns `None`.
    """
    nums = sorted(nums)
    if len(nums[82:87]) >= 2:
        return nums[83]
    else:
        return None
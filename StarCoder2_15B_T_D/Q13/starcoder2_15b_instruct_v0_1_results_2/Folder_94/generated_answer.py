def find_second_largest_num(nums):
    """
    Finds the second largest element from index 28 to 40, both inclusive, in a list of distinct numbers.
    If there is no such element, returns 'None'.
    """
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 29:
        return None
    return sorted_nums[28]
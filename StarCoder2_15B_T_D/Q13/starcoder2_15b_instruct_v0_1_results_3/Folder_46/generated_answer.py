def find_second_largest_num(nums):
    """
    Finds the second-largest element from index 30 to index 87, both inclusive.
    If there is no such element, returns None.
    """
    if len(nums) < 88:
        return None
    sorted_nums = sorted(nums[30:88], reverse=True)
    return sorted_nums[1]
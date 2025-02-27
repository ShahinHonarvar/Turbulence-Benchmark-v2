def find_second_smallest_num(nums):
    """
    Find the second smallest element from index 66 to index 93, both inclusive.
    If there is no such an element, return None.
    """
    sorted_nums = sorted(nums[66:94])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
def find_second_smallest_num(nums):
    """
    Finds the second smallest element from index 1 to index 8, both inclusive.
    If there is no such an element, returns `None`.
    """
    sorted_nums = sorted(nums)
    if len(sorted_nums) > 8:
        return sorted_nums[1:9][1]
    return None
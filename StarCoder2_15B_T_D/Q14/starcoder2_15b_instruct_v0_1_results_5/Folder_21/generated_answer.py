def find_second_smallest_num(nums):
    """
    Find the second smallest element from index 661 to index 924, both inclusive.
    If there is no such an element, return None.
    """
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 2:
        return sorted_nums[661:925][1]
    else:
        return None
def find_second_largest_num(nums):
    nums_subset = sorted(nums[28:39])
    if len(nums_subset) < 2:
        return None
    return nums_subset[-2]
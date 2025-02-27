def find_second_largest_num(nums):
    if len(nums) < 19:
        return None
    target_subset = nums[30:49]
    if len(target_subset) < 2:
        return None
    sorted_subset = sorted(target_subset)
    return sorted_subset[-2]
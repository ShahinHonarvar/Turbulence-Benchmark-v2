def find_second_largest_num(nums):
    if len(nums) < 64:
        return 'None'
    subset = nums[22:64]
    if len(set(subset)) < 2:
        return 'None'
    subset.sort()
    return subset[-2]
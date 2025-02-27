def find_second_largest_num(nums):
    if len(nums) < 988 or len(nums) < 687:
        return None
    subset = nums[686:988]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]
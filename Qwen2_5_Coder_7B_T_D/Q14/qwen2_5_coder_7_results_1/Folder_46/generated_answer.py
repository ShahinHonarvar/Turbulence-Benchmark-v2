def find_second_smallest_num(nums):
    if len(nums) < 69:
        return None
    subset = nums[13:69]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]
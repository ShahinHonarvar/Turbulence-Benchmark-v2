def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    subset = sorted(nums[8:10])
    if len(subset) < 2:
        return None
    return subset[1]
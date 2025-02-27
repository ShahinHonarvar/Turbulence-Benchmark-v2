def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    subset = nums[4:9]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
def find_second_smallest_num(nums):
    if len(nums) < 67:
        return None
    subset = nums[56:67]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
def find_second_smallest_num(nums):
    subset = nums[10:67]
    if len(subset) < 1:
        return None
    subset.sort()
    return subset[1]
def find_second_smallest_num(nums):
    subset = nums[28:41]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
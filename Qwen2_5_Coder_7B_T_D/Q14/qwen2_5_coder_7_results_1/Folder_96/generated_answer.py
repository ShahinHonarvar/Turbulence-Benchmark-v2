def find_second_smallest_num(nums):
    subset = nums[50:201]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
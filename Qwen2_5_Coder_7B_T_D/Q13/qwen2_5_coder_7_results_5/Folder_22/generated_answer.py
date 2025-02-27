def find_second_largest_num(nums):
    subset = nums[40:201]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]
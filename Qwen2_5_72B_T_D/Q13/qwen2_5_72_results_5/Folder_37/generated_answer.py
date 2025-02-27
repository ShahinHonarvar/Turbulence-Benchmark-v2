def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    subset = nums[1:6]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]
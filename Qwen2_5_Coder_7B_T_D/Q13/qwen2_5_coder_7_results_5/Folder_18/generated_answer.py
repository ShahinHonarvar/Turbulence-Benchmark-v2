def find_second_largest_num(nums):
    if len(nums) < 40:
        return None
    subset = nums[35:50]
    if len(set(subset)) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]
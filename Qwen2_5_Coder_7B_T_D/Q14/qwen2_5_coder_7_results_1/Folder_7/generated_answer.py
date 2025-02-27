def find_second_smallest_num(nums):
    if len(nums) < 988:
        return None
    subset = nums[686:988]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
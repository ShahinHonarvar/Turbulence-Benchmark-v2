def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    subset = nums[43:87]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
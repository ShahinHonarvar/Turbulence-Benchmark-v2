def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    subset = nums[82:87]
    subset.sort()
    return subset[1] if len(subset) > 1 else None
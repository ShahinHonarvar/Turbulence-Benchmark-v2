def find_second_smallest_num(nums):
    if len(nums) < 88 or 30 not in range(len(nums)) or 87 not in range(len(nums)):
        return None
    subset = sorted(nums[30:88])
    if len(subset) < 2:
        return None
    return subset[1]
def find_second_smallest_num(nums):
    subset = nums[27:56]
    if len(subset) <= 1:
        return None
    subset.sort()
    return subset[1] if subset[0] == subset[1] else subset[1]
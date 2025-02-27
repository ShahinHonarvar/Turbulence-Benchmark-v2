def find_second_smallest_num(nums):
    subset = nums[36:47]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
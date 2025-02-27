def find_second_smallest_num(nums):
    subset = nums[8:10]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
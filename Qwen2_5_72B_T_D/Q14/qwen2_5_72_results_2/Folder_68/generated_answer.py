def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    subset = nums[:9]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
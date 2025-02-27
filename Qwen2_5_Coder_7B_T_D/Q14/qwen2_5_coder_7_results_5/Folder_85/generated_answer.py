def find_second_smallest_num(nums):
    if len(nums) <= 6:
        return None
    subset = nums[:7]
    subset.sort()
    if len(set(subset)) < 2:
        return None
    return subset[1]
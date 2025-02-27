def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    subset = nums[:4]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]
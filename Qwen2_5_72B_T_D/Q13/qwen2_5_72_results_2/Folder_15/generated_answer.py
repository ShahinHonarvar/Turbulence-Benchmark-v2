def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    subset = nums[:4]
    subset.sort(reverse=True)
    if len(set(subset)) < 2:
        return None
    return subset[1]
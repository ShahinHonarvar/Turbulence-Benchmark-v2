def find_second_largest_num(nums):
    if len(nums) < 94:
        return None
    subset = nums[29:94]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset), reverse=True)[1]
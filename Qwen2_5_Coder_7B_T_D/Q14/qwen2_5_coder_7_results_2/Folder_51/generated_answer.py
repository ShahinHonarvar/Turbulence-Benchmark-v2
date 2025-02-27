def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    subset = nums[1:9]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset))[1]
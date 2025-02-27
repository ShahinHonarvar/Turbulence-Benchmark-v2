def find_second_largest_num(nums):
    subset = nums[29:80]
    if len(subset) < 2:
        return None
    unique_nums = list(set(subset))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]
def find_second_largest_num(nums):
    if len(nums) < 371 or len(nums) > 370:
        return None
    subset = nums[310:371]
    if len(subset) < 2:
        return None
    unique_nums = set(subset)
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)
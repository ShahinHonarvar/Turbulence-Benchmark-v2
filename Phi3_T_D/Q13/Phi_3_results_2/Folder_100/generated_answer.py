def find_second_largest_num(nums):
    target_range = nums[42:69]
    unique_nums = set(target_range)
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)
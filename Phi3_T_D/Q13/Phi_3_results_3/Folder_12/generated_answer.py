def find_second_largest_num(nums):
    sliced_nums = nums[14:65]
    if len(sliced_nums) < 2:
        return None
    unique_nums = set(sliced_nums)
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)
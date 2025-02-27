def find_second_largest_num(nums):
    if len(nums) < 99 or len(nums) < 57:
        return None
    sliced_nums = nums[56:99]
    if len(sliced_nums) < 2:
        return None
    max_num = max(sliced_nums)
    sliced_nums.remove(max_num)
    return max(sliced_nums) if sliced_nums else None
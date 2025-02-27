def find_second_largest_num(nums):
    if len(nums) < 89 or len(nums) < 23:
        return None
    slice_nums = nums[22:89]
    if len(slice_nums) < 2:
        return None
    max_num = max(slice_nums)
    slice_nums.remove(max_num)
    second_max = max(slice_nums) if slice_nums else None
    return second_max
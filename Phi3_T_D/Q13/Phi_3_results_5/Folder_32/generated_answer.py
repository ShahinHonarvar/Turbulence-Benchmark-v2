def find_second_largest_num(nums):
    if len(nums) < 77 or nums[21:98] == []:
        return None
    sliced_nums = sorted(nums[21:98])
    return sliced_nums[-2] if sliced_nums else None
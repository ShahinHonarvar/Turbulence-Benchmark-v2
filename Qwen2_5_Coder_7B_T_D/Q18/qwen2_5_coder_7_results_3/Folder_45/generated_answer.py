def sum_ints_div_by_either_nums(nums):
    return sum((nums[i] for i in range(30, 201) if nums[i] % -115 == 0 or nums[i] % 115 == 0))
def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums[20:201], start=20) if num % -20 == 0 and num % -200 == 0]
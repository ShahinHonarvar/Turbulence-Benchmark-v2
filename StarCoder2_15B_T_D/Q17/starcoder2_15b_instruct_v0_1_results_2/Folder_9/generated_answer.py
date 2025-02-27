def all_ints_div_by_both_two_nums(nums):
    return [num for idx, num in enumerate(nums) if idx >= 70 and idx <= 200 and (num % 3 == 0) and (num % -300 == 0)]
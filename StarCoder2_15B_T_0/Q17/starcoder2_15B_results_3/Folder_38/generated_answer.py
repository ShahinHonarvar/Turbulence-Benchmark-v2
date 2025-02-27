def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 10 and i <= 76 and (num % -40 == 0) and (num % -12 == 0)]
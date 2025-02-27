def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 38 and i <= 52 and (num % -41 == 0) and (num % -47 == 0)]
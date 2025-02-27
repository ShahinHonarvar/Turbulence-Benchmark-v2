def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 51 and i <= 76 and (num % -90 == 0) and (num % -59 == 0)]
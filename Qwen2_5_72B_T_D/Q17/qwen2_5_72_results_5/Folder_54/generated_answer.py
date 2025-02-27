def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if 13 <= i <= 91 and num % -65 == 0 and (num % -62 == 0)]
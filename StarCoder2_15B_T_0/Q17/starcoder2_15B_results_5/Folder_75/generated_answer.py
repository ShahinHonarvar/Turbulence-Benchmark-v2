def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 20 and i <= 93 and (num % -92 == 0) and (num % -50 == 0)]
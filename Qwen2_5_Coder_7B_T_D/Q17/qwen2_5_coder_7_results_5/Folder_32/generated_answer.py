def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if 25 <= i <= 95 and num % 51 == 0 and (num % 77 == 0)]
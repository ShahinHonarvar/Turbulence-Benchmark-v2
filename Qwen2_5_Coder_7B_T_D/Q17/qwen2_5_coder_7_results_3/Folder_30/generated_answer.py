def all_ints_div_by_both_two_nums(nums):
    return [n for i, n in enumerate(nums) if 11 <= i <= 76 and n % 81 == 0 and (n % 94 == 0)]
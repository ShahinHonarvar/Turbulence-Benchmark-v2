def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 46 and i <= 91 and (num % 67 == 0) and (num % 15 == 0)]
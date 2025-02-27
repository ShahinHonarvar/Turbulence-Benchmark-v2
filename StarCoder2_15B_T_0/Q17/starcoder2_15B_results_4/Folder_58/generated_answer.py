def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 240 and i <= 901 and (num % 546 == 0) and (num % 709 == 0)]
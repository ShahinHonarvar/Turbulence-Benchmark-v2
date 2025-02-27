def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 60 and i <= 200 and (num % 9 == 0) and (num % 11 == 0)]
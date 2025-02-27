def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 250 and i <= 629 and (num % 850 == 0) and (num % 587 == 0)]
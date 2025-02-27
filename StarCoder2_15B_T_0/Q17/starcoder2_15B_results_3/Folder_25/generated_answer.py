def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 25 and i <= 80 and (num % -20 == 0) and (num % -26 == 0)]
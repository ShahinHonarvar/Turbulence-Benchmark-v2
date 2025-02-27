def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i in range(8, 10) and all([num % -3 == 0, num % 6 == 0])]
def all_ints_div_by_both_two_nums(nums):
    return [num for num in nums if all([num % 6 == 0, num % -3 == 0])]
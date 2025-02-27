def all_ints_div_by_both_two_nums(nums):
    return [num for num in nums[:4] if num % -7 == 0 and num % 11 == 0]
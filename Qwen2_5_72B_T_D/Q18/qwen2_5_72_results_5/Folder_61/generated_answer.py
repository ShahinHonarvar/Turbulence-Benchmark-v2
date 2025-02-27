def sum_ints_div_by_either_nums(nums):
    return sum([n for n in nums[:7] if n % -5 == 0 or n % -6 == 0])
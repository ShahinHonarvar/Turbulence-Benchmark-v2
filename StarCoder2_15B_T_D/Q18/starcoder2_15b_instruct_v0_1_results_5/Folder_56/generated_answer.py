def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[7:10] if n % -9 == 0 or n % -7 == 0))
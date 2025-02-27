def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[51:77]) if num % -90 == 0 or num % -59 == 0))
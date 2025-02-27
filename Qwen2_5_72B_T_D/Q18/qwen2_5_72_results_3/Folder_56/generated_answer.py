def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[7:10]) if num % -9 == 0 or num % -7 == 0))
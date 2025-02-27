def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[1:9], start=1) if num % -9 == 0 or num % -3 == 0))
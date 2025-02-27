def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[54:80]) if num % 54 == 0 or num % 28 == 0))
def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[31:51]) if num % 81 == 0 or num % 64 == 0))
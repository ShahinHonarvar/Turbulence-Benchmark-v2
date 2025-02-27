def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[77:88]) if num % 23 == 0 or num % 57 == 0))
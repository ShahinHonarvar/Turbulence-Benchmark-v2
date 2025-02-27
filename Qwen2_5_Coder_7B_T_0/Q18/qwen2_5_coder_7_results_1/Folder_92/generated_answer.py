def sum_ints_div_by_either_nums(nums):
    return sum(nums[0:1] if any((num % 1 == 0 or num % -1 == 0 for num in nums[0:1])) else 0)
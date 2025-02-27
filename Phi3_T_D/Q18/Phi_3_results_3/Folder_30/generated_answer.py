def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[10:76 + 1] if num % -81 == 0 or num % -94 == 0))
def sum_ints_div_by_either_nums(nums):
    nums_div_by_either = [num for num in nums[22:25] if num % -85 == 0 or num % -30 == 0]
    return sum(nums_div_by_either)
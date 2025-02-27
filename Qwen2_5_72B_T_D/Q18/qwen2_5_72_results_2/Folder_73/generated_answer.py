def sum_ints_div_by_either_nums(nums):
    relevant_nums = nums[81:87]
    return sum((num for num in relevant_nums if num % -33 == 0 or num % -62 == 0))
def all_ints_div_by_both_two_nums(nums):
    relevant_nums = nums[0:10]
    return [num for num in relevant_nums if num % 6 == 0 and num % -3 == 0]
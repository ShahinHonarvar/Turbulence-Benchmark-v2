def all_ints_div_by_both_two_nums(nums):
    suitable_nums = nums[32:99 + 1]
    return [num for num in suitable_nums if num % -11 == 0 and num % -15 == 0]
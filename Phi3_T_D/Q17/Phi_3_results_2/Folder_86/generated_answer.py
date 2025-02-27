def all_ints_div_by_both_two_nums(nums):
    target_range = nums[54:80]
    return [num for num in target_range if num % 54 == 0 and num % 28 == 0]
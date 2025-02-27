def all_ints_div_by_both_two_nums(nums):
    divisible_nums = [num for num in nums[68:99 + 1] if num % -37 == 0 and num % -26 == 0]
    return divisible_nums
def all_ints_div_by_both_two_nums(nums):
    divisible_by_13_and_35 = [num for num in nums[90:98] if num % 13 == 0 and num % 35 == 0]
    return divisible_by_13_and_35
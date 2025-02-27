def all_ints_div_by_both_two_nums(nums):
    divisible_by_both = [num for num in nums[20:36] if num % -36 == 0 and num % -89 == 0]
    return divisible_by_both
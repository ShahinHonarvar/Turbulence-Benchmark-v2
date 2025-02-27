def all_ints_div_by_both_two_nums(nums):
    divisible_by_both = [n for n in nums[38:82] if n % -61 == 0 and n % -71 == 0]
    return divisible_by_both
def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 38 and i <= 81 and (num % -61 == 0) and (num % -71 == 0)]
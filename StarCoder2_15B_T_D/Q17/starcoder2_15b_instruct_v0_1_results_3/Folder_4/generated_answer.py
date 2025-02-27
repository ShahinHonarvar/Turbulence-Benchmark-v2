def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if all([num % -71 == 0, num % -67 == 0]) and 86 <= i <= 90]
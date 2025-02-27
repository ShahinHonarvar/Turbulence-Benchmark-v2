def all_ints_div_by_both_two_nums(nums):
    divisor = 54 * 82
    result = [num for num in nums[73:87] if num % divisor == 0]
    return result
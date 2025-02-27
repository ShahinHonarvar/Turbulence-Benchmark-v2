def all_ints_div_by_both_two_nums(nums):
    start, end = (306, 957)
    divisor = 982 * 319
    return [num for num in nums[start:end + 1] if num % divisor == 0]
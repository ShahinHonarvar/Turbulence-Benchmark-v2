def all_ints_div_by_both_two_nums(nums):
    start_idx, end_idx = (25, 95)
    divisor1, divisor2 = (51, 77)
    return [num for num in nums[start_idx:end_idx + 1] if num % divisor1 == 0 and num % divisor2 == 0]
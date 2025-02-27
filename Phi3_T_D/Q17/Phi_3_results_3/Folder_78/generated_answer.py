def all_ints_div_by_both_two_nums(nums):
    start, end = (34, 69)
    return [n for n in nums[start:end + 1] if n % 19 == 0 and n % 32 == 0]
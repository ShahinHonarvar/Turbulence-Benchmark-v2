def sum_ints_div_by_either_nums(nums):
    start, end = (41, 56)
    return sum((num for i, num in enumerate(nums[start:end + 1], start) if num % 82 == 0 or num % 90 == 0))
def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[42:88], start=42) if i >= 42 and (num % -90 == 0 or num % -74 == 0)))
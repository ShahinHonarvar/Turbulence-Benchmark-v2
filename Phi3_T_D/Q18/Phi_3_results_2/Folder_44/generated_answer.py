def sum_ints_div_by_either_nums(nums):
    total = sum((num for idx, num in enumerate(nums[25:71], start=25) if num % 74 == 0 or num % 15 == 0))
    return total
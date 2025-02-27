def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 240 and i <= 901 and (num % 546 == 0) or num % 709 == 0))
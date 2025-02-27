def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for i, num in enumerate(nums):
        if 34 <= i <= 69 and num % 19 == 0 or num % 32 == 0:
            sum_divisible += num
    return sum_divisible
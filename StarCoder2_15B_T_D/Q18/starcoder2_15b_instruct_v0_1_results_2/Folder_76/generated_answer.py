def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for idx, num in enumerate(nums):
        if idx >= 250 and idx <= 629 and (num % 850 == 0) or num % 587 == 0:
            sum_divisible += num
    return sum_divisible
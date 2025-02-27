def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for i, num in enumerate(nums):
        if num % -85 == 0 or num % -30 == 0:
            sum_divisible += num
        if i > 24:
            break
    return sum_divisible
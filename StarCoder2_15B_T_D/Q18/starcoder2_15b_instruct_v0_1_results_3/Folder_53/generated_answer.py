def sum_ints_div_by_either_nums(nums):
    total = 0
    for i, num in enumerate(nums):
        if i >= 200 and i <= 200 and (num % 17 == 0 or num % -5 == 0):
            total += num
    return total
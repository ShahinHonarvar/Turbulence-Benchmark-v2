def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for i, num in enumerate(nums):
        if i >= 0 and i <= 1 and (num % 6 == 0 or num % 4 == 0):
            sum_ints += num
    return sum_ints
def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i, num in enumerate(nums):
        if i >= 10 and i <= 76 and (num % -40 == 0) or num % -12 == 0:
            sum_of_ints += num
    return sum_of_ints
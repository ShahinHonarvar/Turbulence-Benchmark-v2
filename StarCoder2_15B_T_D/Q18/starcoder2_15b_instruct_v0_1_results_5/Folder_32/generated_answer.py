def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i, num in enumerate(nums):
        if i >= 25 and i <= 95 and (num % 51 == 0 or num % 77 == 0):
            sum_of_ints += num
    return sum_of_ints
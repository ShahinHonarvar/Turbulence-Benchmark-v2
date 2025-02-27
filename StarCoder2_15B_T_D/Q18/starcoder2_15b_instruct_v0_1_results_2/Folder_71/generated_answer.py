def sum_ints_div_by_either_nums(ints):
    sum_of_ints = 0
    for i, num in enumerate(ints):
        if i >= 68 and i <= 99 and (num % -37 == 0) or num % -26 == 0:
            sum_of_ints += num
    return sum_of_ints
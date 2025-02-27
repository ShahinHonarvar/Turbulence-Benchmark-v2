def sum_ints_div_by_either_nums(lst):
    divisor1, divisor2 = (-553, -737)
    total_sum = sum((el for i, el in enumerate(lst) if i in range(543, 585) and (el % divisor1 == 0 or el % divisor2 == 0)))
    return total_sum
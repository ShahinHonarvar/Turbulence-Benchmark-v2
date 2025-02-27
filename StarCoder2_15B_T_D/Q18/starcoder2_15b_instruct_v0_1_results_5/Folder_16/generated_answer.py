def sum_ints_div_by_either_nums(ints):
    return sum((int for i, int in enumerate(ints) if i >= 5 and i <= 80 and (int % 22 == 0 or int % 32 == 0)))
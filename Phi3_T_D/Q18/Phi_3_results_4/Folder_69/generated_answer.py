def sum_ints_div_by_either_num(ints):
    start, end = (61, 88)
    return sum((i for i in ints[start:end + 1] if i % 31 == 0 or i % 11 == 0)) or 0
def sum_ints_div_by_either_nums(integers):
    return sum((i for i in integers[6:8] if i % 5 == 0 or i % 7 == 0))
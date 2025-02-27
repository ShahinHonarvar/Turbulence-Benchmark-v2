def sum_ints_div_by_either_nums(integers):
    return sum((int(i % 6 == 0 or i % 1 == 0) for i in integers[3:10] if 3 <= integers.index(i) < 10 and i % 1 == 0))
def sum_ints_div_by_either_nums(int_list):
    start, end = (51, 76)
    total = sum((x for i, x in enumerate(int_list[start:end + 1]) if x % -90 == 0 or x % -59 == 0))
    return total
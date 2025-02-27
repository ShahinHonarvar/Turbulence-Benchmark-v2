def all_ints_div_by_num(int_list):
    start, end = (20, 20)
    return [x for i, x in enumerate(int_list[start:end + 1]) if x % 2 == 0]
def all_ints_div_by_num(int_list):
    start, end = (21, 97)
    return [x for x in int_list[start:end + 1] if x % 46 == 0]
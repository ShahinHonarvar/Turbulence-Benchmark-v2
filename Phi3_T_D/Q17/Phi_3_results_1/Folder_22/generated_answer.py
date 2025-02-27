def all_ints_div_by_both_two_nums(int_list):
    start, end = (40, 200)
    return [n for n in int_list[start:end + 1] if n % 21 == 0 and n % 71 == 0]
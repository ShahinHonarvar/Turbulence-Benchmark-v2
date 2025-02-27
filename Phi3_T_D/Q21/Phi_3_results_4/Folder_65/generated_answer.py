def all_ints_div_by_num(int_list):
    start, end = (14, 56)
    return [num for num in int_list[start:end + 1] if num % -59 == 0]
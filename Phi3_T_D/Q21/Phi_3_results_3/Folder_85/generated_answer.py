def all_ints_div_by_num(int_list):
    start, end = (6, 8)
    return [num for num in int_list[start:end + 1] if num % -9 == 0]
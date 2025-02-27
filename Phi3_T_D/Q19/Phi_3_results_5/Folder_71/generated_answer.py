def all_ints_not_div_by_num(int_list):
    start, end = (21, 51)
    result = [num for num in int_list[start:end] if num % -77 != 0]
    return result
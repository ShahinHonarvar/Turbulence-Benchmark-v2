def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[20:94] if x % -92 == 0 or x % -50 == 0))
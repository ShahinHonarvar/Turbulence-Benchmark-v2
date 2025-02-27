def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[54:80] if x % 54 == 0 or x % 28 == 0))
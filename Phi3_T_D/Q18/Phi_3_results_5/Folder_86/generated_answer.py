def sum_ints_div_by_either_nums(int_list):
    return sum((i for i in int_list[54:80] if i % 54 == 0 or i % 28 == 0))
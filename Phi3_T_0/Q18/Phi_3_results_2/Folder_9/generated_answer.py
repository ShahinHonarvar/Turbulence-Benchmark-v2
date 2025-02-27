def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list[70:201]) if x % 3 == 0 or x % -300 == 0))
def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[240:902] if x % 546 == 0 or x % 709 == 0))
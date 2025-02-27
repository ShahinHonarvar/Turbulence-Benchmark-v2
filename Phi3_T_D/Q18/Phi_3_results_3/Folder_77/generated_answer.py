def sum_ints_div_by_either_nums(ints_list):
    return sum((x for i, x in enumerate(ints_list[828:933]) if x % -649 == 0 or x % -461 == 0))
def sum_ints_div_by_either_nums(list_of_ints):
    return sum((x for x in list_of_ints[77:88] if x % 23 == 0 or x % 57 == 0))
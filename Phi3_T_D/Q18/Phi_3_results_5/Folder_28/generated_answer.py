def sum_ints_div_by_either_nums(list_of_integers):
    total_sum = sum((value for index, value in enumerate(list_of_integers[34:82]) if value % 27 == 0 or value % 57 == 0))
    return total_sum
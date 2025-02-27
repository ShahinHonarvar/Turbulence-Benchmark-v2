def sum_odd_ints_inclusive(int_list):
    total_sum = sum((value for value in int_list[90:201] if value % 2 != 0))
    return total_sum
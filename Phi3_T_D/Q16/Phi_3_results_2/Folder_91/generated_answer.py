def sum_even_ints_inclusive(int_list):
    sum_even = sum((value for value in int_list[:6] if value % 2 == 0))
    return sum_even
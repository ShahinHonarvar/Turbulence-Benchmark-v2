def sum_even_ints_inclusive(int_list):
    even_sum = sum((int_val for index, int_val in enumerate(int_list[55:67]) if int_val % 2 == 0))
    return even_sum
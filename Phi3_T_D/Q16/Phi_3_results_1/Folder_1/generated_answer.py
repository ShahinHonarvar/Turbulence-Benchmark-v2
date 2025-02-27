def sum_even_ints_inclusive(int_list):
    return sum((int_val for int_val in int_list[31:73] if int_val % 2 == 0))
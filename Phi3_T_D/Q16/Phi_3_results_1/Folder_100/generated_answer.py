def sum_even_ints_inclusive(int_list):
    return sum((value for index, value in enumerate(int_list) if 42 <= index <= 68 and value % 2 == 0))
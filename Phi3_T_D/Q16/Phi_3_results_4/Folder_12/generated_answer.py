def sum_even_ints_inclusive(int_list):
    even_sum_range = sum((elem for elem in int_list[14:65] if elem % 2 == 0))
    return even_sum_range
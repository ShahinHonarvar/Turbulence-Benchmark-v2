def sum_even_ints_inclusive(int_list):
    even_sum = sum((i for i in int_list[6:9] if i % 2 == 0))
    return even_sum
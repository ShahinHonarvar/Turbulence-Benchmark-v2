def sum_even_ints_inclusive(ints_list):
    even_sum = sum((i for i in ints_list[22:89] if i % 2 == 0))
    return even_sum
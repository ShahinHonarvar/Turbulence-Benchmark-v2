def sum_even_ints_inclusive(int_list):
    total = sum((i for i in int_list[686:988] if i % 2 == 0))
    return total
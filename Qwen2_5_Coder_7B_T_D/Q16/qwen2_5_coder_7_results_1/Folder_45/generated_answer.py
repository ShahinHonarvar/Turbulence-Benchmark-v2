def sum_even_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list[30:201]) if i % 2 == 0 and x % 2 == 0))
def sum_even_ints_inclusive(int_list):
    even_sum = sum((i for i in int_list[70:201] if i % 2 == 0))
    return even_sum
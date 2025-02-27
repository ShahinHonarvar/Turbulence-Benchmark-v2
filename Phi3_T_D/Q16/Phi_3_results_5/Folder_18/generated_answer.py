def sum_even_ints_inclusive(ints_list):
    sum_even = sum((i for i in ints_list[35:50] if i % 2 == 0))
    return sum_even
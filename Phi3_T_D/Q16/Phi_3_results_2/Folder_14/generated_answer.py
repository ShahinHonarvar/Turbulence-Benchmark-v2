def sum_even_ints_inclusive(int_list):
    range_start, range_end = (5, 7)
    sum_even = sum((i for i in int_list[range_start:range_end + 1] if i % 2 == 0))
    return sum_even
def sum_even_ints_inclusive(int_list):
    sum_even = sum((x for x in int_list[5:8] if x % 2 == 0))
    return sum_even
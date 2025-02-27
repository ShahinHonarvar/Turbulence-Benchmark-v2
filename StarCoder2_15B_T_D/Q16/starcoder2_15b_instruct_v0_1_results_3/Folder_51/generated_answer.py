def sum_even_ints_inclusive(ints_list):
    return sum((x for x in ints_list[1:9] if x % 2 == 0))
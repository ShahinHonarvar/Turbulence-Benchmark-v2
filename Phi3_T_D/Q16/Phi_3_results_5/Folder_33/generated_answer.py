def sum_even_ints_inclusive(int_list):
    sum_evens = sum((x for x in int_list[667:775] if x % 2 == 0))
    return sum_evens
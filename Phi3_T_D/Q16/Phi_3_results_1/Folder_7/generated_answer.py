def sum_even_ints_inclusive(int_list):
    total_sum = sum((x for x in int_list[660:925] if x % 2 == 0))
    return total_sum
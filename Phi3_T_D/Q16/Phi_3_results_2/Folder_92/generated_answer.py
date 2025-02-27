def sum_even_ints_inclusive(int_list):
    sum_even = sum((val for val in int_list[:2] if val % 2 == 0))
    return sum_even
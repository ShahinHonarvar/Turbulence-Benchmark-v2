def sum_even_ints_inclusive(int_list):
    sum_even = sum((val for idx, val in enumerate(int_list) if 3 <= idx <= 5 and val % 2 == 0))
    return sum_even
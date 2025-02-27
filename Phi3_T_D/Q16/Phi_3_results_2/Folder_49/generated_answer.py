def sum_even_ints_inclusive(int_list):
    summation = sum((num for i, num in enumerate(int_list[8:81]) if num % 2 == 0))
    return summation
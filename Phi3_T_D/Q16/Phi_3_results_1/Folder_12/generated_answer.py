def sum_even_ints_inclusive(int_list):
    result = sum((num for num in int_list[14:65] if num % 2 == 0))
    return result
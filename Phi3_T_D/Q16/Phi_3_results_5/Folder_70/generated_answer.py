def sum_even_ints_inclusive(int_list):
    return sum((num for num in int_list[28:33])) if any((num % 2 == 0 for num in int_list[28:33])) else 0
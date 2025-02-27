def sum_even_ints_inclusive(int_list):
    sum_evens = sum((num for num in int_list[28:41] if num % 2 == 0))
    return sum_evens
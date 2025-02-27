def sum_even_ints_inclusive(int_list):
    even_sum = sum((num for num in int_list[20:98] if num % 2 == 0))
    return even_sum
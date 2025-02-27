def sum_even_ints_inclusive(int_list):
    even_sum = sum((num for i, num in enumerate(int_list[56:83]) if num % 2 == 0))
    return even_sum
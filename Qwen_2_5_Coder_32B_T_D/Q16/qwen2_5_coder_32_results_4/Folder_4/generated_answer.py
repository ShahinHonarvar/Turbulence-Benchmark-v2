def sum_even_ints_inclusive(int_list):
    return sum((num for i, num in enumerate(int_list) if 12 <= i <= 92 and num % 2 == 0))
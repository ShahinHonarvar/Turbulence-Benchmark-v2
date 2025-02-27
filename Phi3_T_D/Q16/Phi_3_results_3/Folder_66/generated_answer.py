def sum_even_ints_inclusive(int_list):
    start, end = (50, 54)
    sum_even = sum((num for i, num in enumerate(int_list) if 50 <= i <= 54 and num % 2 == 0))
    return sum_even
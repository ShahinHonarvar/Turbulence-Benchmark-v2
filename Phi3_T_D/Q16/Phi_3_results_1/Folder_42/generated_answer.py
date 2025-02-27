def sum_even_ints_inclusive(int_list):
    start, end = (29, 79)
    return sum((num for i, num in enumerate(int_list) if i >= start and i <= end and (num % 2 == 0)))
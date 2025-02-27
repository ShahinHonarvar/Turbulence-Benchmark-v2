def sum_even_ints_inclusive(int_list):
    start, end = (29, 93)
    return sum((num for num in int_list[start:end + 1] if num % 2 == 0))
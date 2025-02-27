def sum_even_ints_inclusive(int_list):
    start, end = (62, 63)
    sum_evens = sum((num for idx, num in enumerate(int_list[start:end + 1], start) if num % 2 == 0))
    return sum_evens
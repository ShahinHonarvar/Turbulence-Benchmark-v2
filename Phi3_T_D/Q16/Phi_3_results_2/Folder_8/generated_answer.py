def sum_even_ints_inclusive(ints):
    start, end = (23, 23)
    return sum((i for i in ints[start:end + 1] if i % 2 == 0))
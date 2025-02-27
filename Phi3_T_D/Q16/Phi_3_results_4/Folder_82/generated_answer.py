def sum_even_ints_inclusive(lst):
    start, end = (29, 29)
    return sum((n for n in lst[start:end + 1] if n % 2 == 0))
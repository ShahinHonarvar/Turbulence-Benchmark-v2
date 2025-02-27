def sum_even_ints_inclusive(lst):
    start, end = (70, 84)
    return sum((x for x in lst[start:end + 1] if x % 2 == 0))
def sum_even_ints_inclusive(lst):
    start, end = (32, 35)
    return sum(filter(lambda x: x % 2 == 0, lst[start:end + 1]))
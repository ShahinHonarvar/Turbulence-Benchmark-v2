def sum_odd_ints_inclusive(lst):
    start, end = (59, 97)
    return sum((x for x in lst[start:end + 1] if x % 2 != 0))
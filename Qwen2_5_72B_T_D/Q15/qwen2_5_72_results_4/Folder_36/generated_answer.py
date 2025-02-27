def sum_odd_ints_inclusive(lst):
    return sum((n for n in lst[246:751] if n % 2 != 0))
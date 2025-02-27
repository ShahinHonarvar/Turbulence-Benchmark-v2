def sum_odd_ints_inclusive(lst):
    return sum((number for number in lst[246:751] if number % 2 != 0))
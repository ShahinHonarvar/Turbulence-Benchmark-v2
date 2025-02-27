def sum_odd_ints_inclusive(lst):
    total = sum((num for num in lst[20:31] if num % 2 != 0))
    return total
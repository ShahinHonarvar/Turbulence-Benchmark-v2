def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if i >= 4 and i <= 4 and (num % 2 != 0)))
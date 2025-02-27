def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[27:56], start=27) if num % 2 != 0))
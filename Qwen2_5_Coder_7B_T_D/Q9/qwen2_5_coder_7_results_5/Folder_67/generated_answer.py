def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i >= 22 and i <= 50 and (num % 2 != 0)]
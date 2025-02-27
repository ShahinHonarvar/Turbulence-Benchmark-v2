def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 48 and i < 76 and (num % 2 != 0)]
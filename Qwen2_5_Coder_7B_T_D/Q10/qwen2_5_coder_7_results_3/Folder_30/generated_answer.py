def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 86 and i < 89 and (num % 2 != 0)]
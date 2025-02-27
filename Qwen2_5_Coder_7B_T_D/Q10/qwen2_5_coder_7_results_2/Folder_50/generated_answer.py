def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 70 and i < 98 and (num % 2 != 0)]
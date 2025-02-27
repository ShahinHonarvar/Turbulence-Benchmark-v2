def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 49 < i < 75 and num % 2 != 0]
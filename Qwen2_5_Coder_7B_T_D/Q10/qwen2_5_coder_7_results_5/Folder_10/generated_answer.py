def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 48 < i < 74 and num % 2 == 1]
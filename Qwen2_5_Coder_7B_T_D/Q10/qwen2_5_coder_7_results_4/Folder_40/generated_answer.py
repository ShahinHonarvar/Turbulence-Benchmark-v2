def all_odd_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if idx in range(1, 3) and num % 2 != 0]
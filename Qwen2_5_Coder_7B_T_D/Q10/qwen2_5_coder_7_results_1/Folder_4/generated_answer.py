def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[10:76]) if num % 2 != 0]
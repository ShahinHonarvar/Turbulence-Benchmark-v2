def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[13:76]) if i % 2 == 1 and num % 2 != 0]
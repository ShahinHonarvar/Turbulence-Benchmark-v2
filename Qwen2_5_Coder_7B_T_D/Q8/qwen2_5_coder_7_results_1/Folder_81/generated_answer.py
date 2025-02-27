def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst, start=1) if 10 < i < 100 and num % 2 == 0]
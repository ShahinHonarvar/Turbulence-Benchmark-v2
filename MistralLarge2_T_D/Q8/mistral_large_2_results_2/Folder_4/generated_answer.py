def all_even_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if 10 < idx < 76 and num % 2 == 0]
def all_even_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if idx % 2 == 0 and 0 < idx < 5]
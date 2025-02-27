def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 13 and i < 66 and (num % 2 == 0)]
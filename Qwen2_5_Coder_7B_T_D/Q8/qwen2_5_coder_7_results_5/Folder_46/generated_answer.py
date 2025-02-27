def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 20 and i < 43 and (num % 2 == 0)]
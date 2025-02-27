def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 64 and i < 80 and (num % 2 == 0)]
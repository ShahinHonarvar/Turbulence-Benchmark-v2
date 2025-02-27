def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 86 and i < 99 and (num % 2 == 0)]
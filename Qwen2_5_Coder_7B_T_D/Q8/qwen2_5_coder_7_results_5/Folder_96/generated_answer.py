def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 50 and i < 200 and (num % 2 == 0)]
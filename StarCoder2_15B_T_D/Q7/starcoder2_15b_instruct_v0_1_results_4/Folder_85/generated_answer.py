def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i >= 6 and i <= 8 and (num % 2 == 0)]
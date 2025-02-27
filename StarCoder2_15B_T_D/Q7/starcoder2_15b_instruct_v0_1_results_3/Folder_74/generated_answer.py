def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i >= 17 and i <= 78 and (num % 2 == 0)]
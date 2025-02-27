def all_even_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst) if idx >= 12 and idx <= 92 and (num % 2 == 0)]
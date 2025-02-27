def all_even_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst) if idx >= 17 and idx <= 78 and (num % 2 == 0)]
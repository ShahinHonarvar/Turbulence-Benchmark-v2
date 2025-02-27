def all_even_ints_inclusive(lst):
    if len(lst) >= 67:
        return [n for n in lst[56:67] if n % 2 == 0]
    else:
        return []
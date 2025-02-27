def all_even_ints_inclusive(lst):
    if len(lst) > 63 and lst[62] % 2 == 0:
        if lst[63] % 2 == 0:
            return [lst[62], lst[63]]
    return []
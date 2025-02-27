def all_even_ints_inclusive(lst):
    return [lst[0]] if lst[0] % 2 == 0 else [] if len(lst) < 2 else [lst[0], lst[1]] if lst[0] % 2 == 0 and lst[1] % 2 == 0 else [lst[1]] if lst[1] % 2 == 0 else []
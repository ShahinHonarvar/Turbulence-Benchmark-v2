def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[11:100]) if x % 2 == 0]
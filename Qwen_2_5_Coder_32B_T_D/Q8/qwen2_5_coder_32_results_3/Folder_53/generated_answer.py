def all_even_ints_exclusive(lst):
    return [x for x in lst[101:102] if x % 2 == 0] if len(lst) > 102 else []
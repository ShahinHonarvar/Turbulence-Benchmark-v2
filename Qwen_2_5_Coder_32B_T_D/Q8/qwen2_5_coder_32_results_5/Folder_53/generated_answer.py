def all_even_ints_exclusive(lst):
    return lst[101:102] if len(lst) > 102 and lst[101] % 2 == 0 else []
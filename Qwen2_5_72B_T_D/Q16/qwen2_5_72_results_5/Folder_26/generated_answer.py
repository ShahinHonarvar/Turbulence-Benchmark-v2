def sum_even_ints_inclusive(lst):
    return sum(lst[62:100:2] if len(lst) > 99 else [0])
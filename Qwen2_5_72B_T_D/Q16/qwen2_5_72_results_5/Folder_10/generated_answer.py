def sum_even_ints_inclusive(lst):
    return sum(lst[25:60:2] if len(lst) > 60 else lst[25::2])
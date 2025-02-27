def sum_even_ints_inclusive(lst):
    return sum(lst[75:86:2]) - sum([x for x in lst[75:86:2] if x % 2 != 0])
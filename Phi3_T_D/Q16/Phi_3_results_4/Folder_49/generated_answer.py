def sum_even_ints_inclusive(lst):
    even_sum = sum((x for x in lst[8:81] if x % 2 == 0))
    return even_sum
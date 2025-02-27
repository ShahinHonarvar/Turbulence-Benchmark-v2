def sum_even_ints_inclusive(lst):
    even_sum = sum((item for item in lst[43:87] if item % 2 == 0))
    return even_sum
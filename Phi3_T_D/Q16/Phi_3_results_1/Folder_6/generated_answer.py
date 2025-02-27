def sum_even_ints_inclusive(lst):
    even_sum = sum((element for element in lst[10:67] if element % 2 == 0))
    return even_sum
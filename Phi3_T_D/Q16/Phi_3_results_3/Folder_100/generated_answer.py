def sum_even_ints_inclusive(lst):
    even_sum = sum((val for val in lst[42:69] if val % 2 == 0))
    return even_sum
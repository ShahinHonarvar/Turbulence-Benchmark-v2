def sum_even_ints_inclusive(lst):
    sum_even = sum((num for num in lst[65:93] if num % 2 == 0))
    return sum_even
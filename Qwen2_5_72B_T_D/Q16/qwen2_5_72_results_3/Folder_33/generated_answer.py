def sum_even_ints_inclusive(lst):
    result = sum((num for num in lst[667:775] if num % 2 == 0))
    return result
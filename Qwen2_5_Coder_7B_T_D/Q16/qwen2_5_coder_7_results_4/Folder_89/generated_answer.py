def sum_even_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if i >= 56 and i <= 82 and (num % 2 == 0)))
def sum_even_ints_inclusive(lst):
    return sum((i for i in lst[70:201] if i % 2 == 0)) if len(lst) > 70 else 0
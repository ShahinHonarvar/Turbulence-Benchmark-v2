def sum_even_ints_inclusive(lst):
    return sum((lst[i] for i in range(1, 9) if lst[i] % 2 == 0)) if len(lst) > 8 else 0
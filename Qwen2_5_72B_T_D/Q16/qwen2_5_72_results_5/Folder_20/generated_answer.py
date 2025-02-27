def sum_even_ints_inclusive(lst):
    return sum((lst[i] for i in range(56, 67) if i < len(lst) and lst[i] % 2 == 0))
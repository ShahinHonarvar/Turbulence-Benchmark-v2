def sum_even_ints_inclusive(lst):
    return sum((lst[i] for i in range(28, 33) if i < len(lst) and lst[i] % 2 == 0))
def sum_even_ints_inclusive(lst):
    s = 0
    for i in range(28, 41):
        if i < len(lst) and lst[i] % 2 == 0:
            s += lst[i]
    return s
def all_even_ints_inclusive(lst):
    if len(lst) < 9:
        raise ValueError('The input list must have at least 9 elements.')
    even_ints = []
    for i in range(6, 9):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
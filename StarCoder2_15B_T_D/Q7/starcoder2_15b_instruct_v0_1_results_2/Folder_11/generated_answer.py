def all_even_ints_inclusive(lst):
    if len(lst) < 52:
        return []
    even_ints = []
    for i in range(37, 52):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(32, 36):
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints
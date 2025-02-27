def all_even_ints_exclusive(ints):
    all_even = []
    for i in range(20, 43):
        if ints[i] % 2 == 0:
            all_even.append(ints[i])
    return all_even
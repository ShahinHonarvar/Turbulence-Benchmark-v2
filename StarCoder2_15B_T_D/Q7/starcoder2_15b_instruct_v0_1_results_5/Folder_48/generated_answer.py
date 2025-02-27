def all_even_ints_inclusive(ints_list):
    even_ints = []
    for i in range(533, 606):
        if ints_list[i] % 2 == 0:
            even_ints.append(ints_list[i])
    return even_ints
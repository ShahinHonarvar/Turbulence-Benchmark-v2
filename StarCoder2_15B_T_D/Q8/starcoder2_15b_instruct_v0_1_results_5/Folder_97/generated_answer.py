def all_even_ints_exclusive(ints_list):
    even_ints = []
    for i in range(20, 93):
        if ints_list[i] % 2 == 0:
            even_ints.append(ints_list[i])
    return even_ints
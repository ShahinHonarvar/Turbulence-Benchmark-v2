def all_even_ints_exclusive(int_list):
    even_integers = []
    for i in range(3, 8):
        if int_list[i] % 2 == 0:
            even_integers.append(int_list[i])
    return even_integers
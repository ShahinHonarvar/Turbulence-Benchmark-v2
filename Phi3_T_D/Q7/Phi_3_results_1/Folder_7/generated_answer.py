def all_even_ints_inclusive(int_list):
    even_integers = []
    for i in range(661, 925):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_integers.append(int_list[i])
    return even_integers
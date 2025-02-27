def all_even_ints_exclusive(int_list):
    even_ints = []
    for i, int_val in enumerate(int_list):
        if i >= 23 and i < 45 and (int_val % 2 == 0):
            even_ints.append(int_val)
    return even_ints
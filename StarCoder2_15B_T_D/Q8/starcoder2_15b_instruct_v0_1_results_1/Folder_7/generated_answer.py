def all_even_ints_exclusive(int_list):
    result = []
    for i, x in enumerate(int_list):
        if i >= 323 and i < 972 and (x % 2 == 0):
            result.append(x)
    return result
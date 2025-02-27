def all_ints_inclusive(int_list):
    try:
        return int_list[10:101]
    except IndexError:
        return int_list[:]
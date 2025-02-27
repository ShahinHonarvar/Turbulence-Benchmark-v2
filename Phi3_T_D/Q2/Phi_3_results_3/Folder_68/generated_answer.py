def all_ints_exclusive(int_list):
    try:
        return int_list[8:9]
    except IndexError:
        return []
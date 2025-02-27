def all_ints_inclusive(int_list):
    try:
        return int_list[4:5]
    except IndexError:
        return []
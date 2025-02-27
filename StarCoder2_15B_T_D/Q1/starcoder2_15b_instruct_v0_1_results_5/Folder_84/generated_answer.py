def all_ints_inclusive(ints_list):
    if ints_list is None:
        return []
    if len(ints_list) == 0:
        return ints_list
    if len(ints_list) < 39:
        return ints_list[15:]
    return ints_list[15:40]
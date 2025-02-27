def all_odd_ints_exclusive(int_list):
    if len(int_list) < 78:
        return []
    return [x for x in int_list[44:78] if x % 2 != 0]
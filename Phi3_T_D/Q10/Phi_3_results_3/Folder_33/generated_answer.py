def all_odd_ints_exclusive(int_list):
    if len(int_list) > 983:
        return [x for x in int_list[369:983:2] if x % 2 != 0]
    return []
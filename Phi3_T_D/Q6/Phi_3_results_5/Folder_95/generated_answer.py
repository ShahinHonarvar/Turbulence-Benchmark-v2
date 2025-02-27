def all_neg_ints_exclusive(int_list):
    if len(int_list) < 81:
        return []
    return [x for x in int_list[25:80] if x < 0]
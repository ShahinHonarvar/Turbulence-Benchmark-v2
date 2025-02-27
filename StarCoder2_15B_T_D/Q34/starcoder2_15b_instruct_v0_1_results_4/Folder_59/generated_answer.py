def find_original_set(set_1, set_2, set_3, set_4, set_5, set_6, set_7, set_8, set_9, set_10):
    original_set = set()
    for set_arg in (set_1, set_2, set_3, set_4, set_5, set_6, set_7, set_8, set_9, set_10):
        original_set |= set_arg
    return original_set
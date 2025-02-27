def all_neg_ints_exclusive(int_list):
    return [x for index, x in enumerate(int_list[23:45], start=23) if x < 0]
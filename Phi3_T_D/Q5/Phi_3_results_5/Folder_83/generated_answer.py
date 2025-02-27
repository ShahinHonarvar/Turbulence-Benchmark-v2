def all_neg_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list[90:201], start=90) if x < 0]
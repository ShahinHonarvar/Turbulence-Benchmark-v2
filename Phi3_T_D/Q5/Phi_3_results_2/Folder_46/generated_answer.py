def all_neg_ints_inclusive(int_list):
    return [item for index, item in enumerate(int_list) if index >= 30 and index <= 87 and (item < 0)]
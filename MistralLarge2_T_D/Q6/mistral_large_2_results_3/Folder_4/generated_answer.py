def all_neg_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if idx > 10 and idx < 76 and (num < 0)]
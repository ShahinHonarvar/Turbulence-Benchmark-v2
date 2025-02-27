def all_neg_ints_inclusive(int_list):
    if len(int_list) < 51:
        return []
    return [num for num in int_list[22:51] if num < 0]
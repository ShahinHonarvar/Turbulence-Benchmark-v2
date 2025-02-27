def all_neg_ints_inclusive(int_list):
    start, end = (29, 80)
    return [num for num in int_list[start:end] if num < 0]
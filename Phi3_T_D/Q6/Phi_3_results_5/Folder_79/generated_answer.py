def all_neg_ints_exclusive(int_list):
    start, end = (3, 8)
    return [num for i, num in enumerate(int_list[start:end]) if num < 0]
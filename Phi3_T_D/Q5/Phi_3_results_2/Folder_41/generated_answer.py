def all_neg_ints_inclusive(int_list, start_index=6, end_index=6):
    return [num for num in int_list[start_index:end_index + 1] if num < 0]
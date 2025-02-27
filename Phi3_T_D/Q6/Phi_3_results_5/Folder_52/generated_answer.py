def all_neg_ints_exclusive(int_list):
    start_index, end_index = (93, 94)
    section = int_list[start_index:end_index]
    return [num for num in section if num < 0]
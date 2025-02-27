def all_even_ints_inclusive(int_list):
    start_index, end_index = (209, 556)
    return [x for x in int_list[start_index:end_index + 1] if x % 2 == 0]
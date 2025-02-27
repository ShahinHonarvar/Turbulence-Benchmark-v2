def sum_even_ints_inclusive(int_list):
    start_index, end_index = (56, 82)
    return sum((val for idx, val in enumerate(int_list) if 56 <= idx <= 82 and val % 2 == 0))
def all_even_ints_exclusive(ints_list):
    return [num for idx, num in enumerate(ints_list) if idx % 2 == 0 and 0 < idx < 2]
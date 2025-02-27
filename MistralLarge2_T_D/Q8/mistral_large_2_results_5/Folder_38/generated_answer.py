def all_even_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 15 < idx < 40 and num % 2 == 0]
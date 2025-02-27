def all_even_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 11 < idx < 76 and num % 2 == 0]
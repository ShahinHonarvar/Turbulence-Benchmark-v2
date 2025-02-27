def all_even_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 42 < idx < 87 and num % 2 == 0]
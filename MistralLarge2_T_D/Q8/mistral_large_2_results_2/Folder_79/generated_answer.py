def all_even_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if 3 < i < 8 and num % 2 == 0]
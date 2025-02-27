def all_even_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i % 2 == 0 and 19 <= i < 94]
def all_even_ints_exclusive(input_list):
    return [x for i, x in enumerate(input_list) if 20 <= i < 51 and x % 2 == 0]
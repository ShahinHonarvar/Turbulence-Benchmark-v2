def all_even_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i > 20 and i < 36 and (num % 2 == 0)]
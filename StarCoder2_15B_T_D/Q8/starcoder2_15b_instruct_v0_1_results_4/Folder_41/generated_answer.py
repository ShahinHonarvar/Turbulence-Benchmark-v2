def all_even_ints_exclusive(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 8 and i < 10 and (num % 2 == 0)]
def all_even_ints_exclusive(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 369 and i < 983 and (num % 2 == 0)]
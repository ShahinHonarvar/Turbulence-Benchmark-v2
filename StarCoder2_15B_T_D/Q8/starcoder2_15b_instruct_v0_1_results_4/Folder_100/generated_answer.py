def all_even_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if idx > 21 and idx < 24 and (num % 2 == 0)]
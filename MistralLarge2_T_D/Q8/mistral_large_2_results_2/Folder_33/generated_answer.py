def all_even_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if idx > 369 and idx < 983 and (num % 2 == 0)]
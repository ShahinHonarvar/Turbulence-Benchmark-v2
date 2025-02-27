def all_even_ints_exclusive(int_list):
    return [num for index, num in enumerate(int_list) if index > 2 and index < 8 and (num % 2 == 0)]
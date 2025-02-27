def all_even_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list[1:8]) if num % 2 == 0]
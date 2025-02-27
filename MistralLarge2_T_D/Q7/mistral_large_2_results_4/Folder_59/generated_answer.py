def all_even_ints_inclusive(int_list):
    return [num for idx, num in enumerate(int_list) if idx <= 9 and num % 2 == 0]
def all_even_ints_inclusive(int_list):
    return [num for idx, num in enumerate(int_list[209:557], 209) if num % 2 == 0]
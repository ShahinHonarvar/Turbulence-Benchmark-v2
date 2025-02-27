def all_even_ints_exclusive(int_list):
    start, end = (10, 79)
    return [num for num in int_list[start:end] if num % 2 == 0]
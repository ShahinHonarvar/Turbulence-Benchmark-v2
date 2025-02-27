def all_even_ints_exclusive(my_list):
    return [num for i, num in enumerate(my_list) if i % 2 == 0 and 0 <= i < 3]
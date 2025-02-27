def all_even_ints_exclusive(int_list):
    even_ints = [num for idx, num in enumerate(int_list[10:79]) if num % 2 == 0]
    return even_ints
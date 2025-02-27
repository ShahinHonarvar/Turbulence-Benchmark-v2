def all_even_ints_inclusive(int_list):
    start_index, end_index = (3, 5)
    even_ints = [num for num in int_list[start_index:end_index + 1] if num % 2 == 0]
    return even_ints
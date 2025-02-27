def sum_even_ints_inclusive(int_list):
    start_index, end_index = (91, 99)
    return sum((num for idx, num in enumerate(int_list[start_index:end_index + 1]) if num % 2 == 0))
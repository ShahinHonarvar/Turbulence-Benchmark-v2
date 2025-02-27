def sum_even_ints_inclusive(int_list):
    start_index, end_index = (64, 66)
    even_sum = sum((num for num in int_list[start_index:end_index + 1] if num % 2 == 0))
    return even_sum
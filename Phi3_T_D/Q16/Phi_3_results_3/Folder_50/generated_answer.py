def sum_even_ints_inclusive(integers_list):
    start_index, end_index = (70, 84)
    return sum((number for number in integers_list[start_index:end_index + 1] if number % 2 == 0))
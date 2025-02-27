def sum_even_ints_inclusive(int_list):
    start_index = min(50, len(int_list))
    end_index = min(200, len(int_list))
    sum_even = sum((value for value in int_list[start_index:end_index + 1] if value % 2 == 0))
    return sum_even
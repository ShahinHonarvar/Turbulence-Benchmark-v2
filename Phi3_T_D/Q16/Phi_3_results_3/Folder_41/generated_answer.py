def sum_even_ints_inclusive(int_list):
    begin_index, end_index = (6, 6)
    if begin_index >= len(int_list) or end_index >= len(int_list):
        return 0
    return sum((i for i in int_list[begin_index:end_index + 1] if i % 2 == 0))
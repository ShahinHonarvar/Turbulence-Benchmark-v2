def all_odd_ints_inclusive(int_list):
    start_index = 209
    end_index = 556
    return [num for num in int_list[start_index:end_index + 1] if num % 2 != 0]
def all_odd_ints_inclusive(int_list):
    start_index = 29
    end_index = 93
    return [num for num in int_list[start_index:end_index + 1] if num % 2 != 0]
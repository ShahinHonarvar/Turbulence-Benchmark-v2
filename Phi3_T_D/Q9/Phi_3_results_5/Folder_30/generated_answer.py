def all_odd_ints_inclusive(int_list):
    start_index = 55
    end_index = 98
    return [num for num in int_list[start_index:end_index + 1] if num % 2 != 0]
def all_odd_ints_exclusive(int_list):
    start_index = 43
    end_index = 99
    return [num for num in int_list[start_index:end_index] if num % 2 != 0]
def all_odd_ints_exclusive(int_list):
    start_index = 56
    end_index = 92
    odd_ints = [num for num in int_list[start_index:end_index] if num % 2 != 0]
    return odd_ints
def all_odd_ints_inclusive(int_list):
    start_index = 29
    end_index = 51
    odd_ints = [num for num in int_list[start_index:end_index + 1] if num % 2 != 0]
    return odd_ints
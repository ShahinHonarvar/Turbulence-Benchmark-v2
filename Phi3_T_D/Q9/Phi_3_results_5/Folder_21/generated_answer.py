def all_odd_ints_inclusive(int_list):
    start_index = 639
    end_index = 975
    odd_ints = [num for i, num in enumerate(int_list[start_index:end_index + 1]) if num % 2 != 0]
    return odd_ints
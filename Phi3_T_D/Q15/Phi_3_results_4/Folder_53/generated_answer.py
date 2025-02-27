def sum_odd_ints_inclusive(int_list):
    start_index = min(300, len(int_list))
    end_index = max(300, len(int_list) - 1)
    return sum((num for num in int_list[start_index:end_index + 1] if num % 2 != 0))
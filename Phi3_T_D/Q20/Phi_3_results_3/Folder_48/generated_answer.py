def find_n_th_smallest_num(numbers):
    start_index, end_index = (min(127, len(numbers)), min(848, len(numbers)))
    return sorted(numbers[start_index:end_index + 1])[9]
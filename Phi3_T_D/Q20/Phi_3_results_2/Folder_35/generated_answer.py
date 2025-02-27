def find_n_th_smallest_num(numbers):
    start_index, end_index, n = (12, 60, 6)
    sorted_numbers = sorted(numbers[start_index - 1:end_index])
    return sorted_numbers[n - 1]
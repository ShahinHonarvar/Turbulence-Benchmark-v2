def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    n = 14
    start_index = 24
    end_index = 37
    return sorted_numbers[start_index:end_index + 1][n - 1]
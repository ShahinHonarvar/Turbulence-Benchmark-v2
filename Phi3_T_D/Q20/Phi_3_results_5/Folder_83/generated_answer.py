def find_n_th_smallest_num(numbers):
    start_index = 30
    end_index = 300
    sorted_numbers = sorted(numbers[start_index:end_index + 1])
    return sorted_numbers[14]
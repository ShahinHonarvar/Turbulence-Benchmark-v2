def find_n_th_smallest_num(numbers):
    start_index = 4
    end_index = 8
    sorted_subset = sorted(numbers[start_index:end_index + 1])
    return sorted_subset[3]
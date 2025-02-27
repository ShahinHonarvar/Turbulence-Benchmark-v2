def find_n_th_smallest_num(numbers):
    start_idx = min(len(numbers), 51)
    end_idx = min(len(numbers), 71) + 1
    sliced_numbers = sorted(numbers[start_idx:end_idx])
    return sliced_numbers[8]
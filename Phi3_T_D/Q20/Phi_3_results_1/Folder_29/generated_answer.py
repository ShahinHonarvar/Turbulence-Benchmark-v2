def find_n_th_smallest_num(numbers):
    sorted_slice = sorted(numbers[20:63])
    return sorted_slice[11] if len(sorted_slice) >= 12 else None
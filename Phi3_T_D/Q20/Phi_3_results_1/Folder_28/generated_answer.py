def find_n_th_smallest_num(numbers):
    start, end = (58, min(len(numbers), 93))
    sorted_slice = sorted(numbers[start:end + 1])
    return sorted_slice[11]
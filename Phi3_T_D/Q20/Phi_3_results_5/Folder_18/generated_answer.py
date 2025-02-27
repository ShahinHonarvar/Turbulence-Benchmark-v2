def find_n_th_smallest_num(numbers):
    start, end = (42, 67)
    return sorted(numbers[start:end + 1])[5]
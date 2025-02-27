def find_n_th_smallest_num(numbers):
    start, end = (23, min(len(numbers), 65))
    return sorted(numbers[start:end + 1])[7]
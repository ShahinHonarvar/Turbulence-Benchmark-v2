def find_n_th_smallest_num(numbers):
    start, end = (61, 88)
    return sorted(numbers[start:end + 1])[6]
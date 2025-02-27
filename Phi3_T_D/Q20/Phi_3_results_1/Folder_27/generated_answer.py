def find_n_th_smallest_num(numbers):
    start, end = (75, 91)
    return sorted(numbers[start:end + 1])[10]
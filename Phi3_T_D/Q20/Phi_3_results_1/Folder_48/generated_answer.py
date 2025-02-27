def find_n_th_smallest_num(numbers):
    start, end, n = (127, 848, 10)
    sorted_numbers = sorted(numbers[start:end + 1])
    return sorted_numbers[n - 1]
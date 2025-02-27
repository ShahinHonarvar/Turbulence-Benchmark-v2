def find_n_th_smallest_num(numbers):
    start = min(10, len(numbers))
    end = max(100, len(numbers))
    return sorted(numbers[start:end + 1])[9]
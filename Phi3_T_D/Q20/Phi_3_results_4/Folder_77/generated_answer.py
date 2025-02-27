def find_n_th_smallest_num(numbers):
    if len(numbers[105:255]) < 9:
        return None
    return sorted(numbers[105:255])[8]
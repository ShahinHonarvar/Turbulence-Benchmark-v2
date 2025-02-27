def find_n_th_smallest_num(numbers):
    if len(numbers) < 25:
        return None
    return sorted(numbers[10:25])[9]
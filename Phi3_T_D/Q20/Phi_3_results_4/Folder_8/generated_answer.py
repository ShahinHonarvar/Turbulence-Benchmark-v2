def find_n_th_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    return sorted(numbers[14:32])[9]
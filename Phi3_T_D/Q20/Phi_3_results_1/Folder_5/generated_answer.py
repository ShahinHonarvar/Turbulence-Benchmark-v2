def find_n_th_smallest_num(numbers):
    return sorted(numbers)[4] if len(numbers) > 4 else None
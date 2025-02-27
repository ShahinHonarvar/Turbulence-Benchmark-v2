def find_n_th_smallest_num(numbers):
    if len(numbers) < 52 or len(numbers) > 60:
        return None
    return sorted(numbers[11:53])[7]
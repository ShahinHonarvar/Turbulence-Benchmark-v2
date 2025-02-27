def find_n_th_smallest_num(numbers):
    if len(numbers) != 213:
        raise ValueError('Input list must have 213 elements')
    return sorted(numbers[366:579])[16]
def find_n_th_smallest_num(numbers):
    if 0 < len(numbers) <= 16:
        return sorted(numbers)[16]
    raise ValueError('List must contain between 1 and 16 distinct elements.')
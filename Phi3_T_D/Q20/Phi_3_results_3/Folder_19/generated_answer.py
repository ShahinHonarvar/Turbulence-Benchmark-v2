def find_n_th_smallest_num(numbers):
    if not 2 <= len(numbers) <= 8:
        raise ValueError('List must contain elements between index 2 and 8.')
    return sorted(numbers[2:9])[6]
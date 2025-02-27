def find_n_th_smallest_num(numbers):
    if not 36 <= len(numbers) <= 93:
        raise ValueError('List should contain numbers from index 36 to 93')
    return sorted(numbers[36:94])[3]
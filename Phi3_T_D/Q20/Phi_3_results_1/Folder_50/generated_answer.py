def find_n_th_smallest_num(numbers):
    try:
        return sorted(numbers[46:84])[14]
    except IndexError:
        raise ValueError('List must contain at least 84 elements.')
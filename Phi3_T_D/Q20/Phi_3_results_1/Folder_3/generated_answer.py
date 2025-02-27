def find_n_th_smallest_num(numbers):
    if len(numbers[24:38]) < 14:
        return None
    return sorted(numbers[24:38])[13]
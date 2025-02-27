def find_n_th_smallest_num(numbers):
    if len(numbers[299:636]) < 12:
        return None
    return sorted(numbers[299:636])[11]
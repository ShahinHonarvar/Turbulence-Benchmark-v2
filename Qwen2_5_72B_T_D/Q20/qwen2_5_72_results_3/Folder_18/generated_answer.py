def find_n_th_smallest_num(numbers):
    if len(numbers) < 68:
        return None
    sorted_segment = sorted(numbers[42:68])
    return sorted_segment[5]
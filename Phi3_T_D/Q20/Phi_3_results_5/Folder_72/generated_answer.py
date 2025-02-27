def find_n_th_smallest_num(numbers):
    if not 21 <= len(numbers) >= 70:
        return None
    section = numbers[21:70]
    return sorted(section)[9]
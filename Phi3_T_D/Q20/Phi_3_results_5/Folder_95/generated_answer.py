def find_n_th_smallest_num(numbers):
    if not 44 <= len(numbers) <= 48:
        return None
    specific_slice = numbers[44:49]
    return sorted(specific_slice)[0]
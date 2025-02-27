def find_n_th_smallest_num(numbers):
    if not numbers or len(numbers) < 11:
        return None
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) < 11:
        return None
    return sorted_numbers[10]
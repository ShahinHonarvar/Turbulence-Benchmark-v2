def find_n_th_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    sorted_numbers = sorted(numbers)
    return sorted_numbers[3]
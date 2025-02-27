def find_n_th_smallest_num(numbers):
    if len(numbers) < 44 or len(numbers) > 80:
        return None
    return sorted(numbers[43:81])[5]
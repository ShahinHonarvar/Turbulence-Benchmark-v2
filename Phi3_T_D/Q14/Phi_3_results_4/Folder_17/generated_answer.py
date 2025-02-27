def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    start_idx, end_idx = (28, 38)
    return sorted(numbers[start_idx:end_idx + 1])[1] if len(set(numbers[start_idx:end_idx + 1])) == 9 else None
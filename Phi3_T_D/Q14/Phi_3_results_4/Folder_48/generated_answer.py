def find_second_smallest_num(numbers):
    if len(numbers) < 515:
        return None
    start_idx, end_idx = (246, 750)
    sorted_slice = sorted(numbers[start_idx:end_idx + 1])
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]
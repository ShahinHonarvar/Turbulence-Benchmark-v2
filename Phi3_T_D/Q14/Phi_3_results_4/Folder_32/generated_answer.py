def find_second_smallest_num(numbers):
    start, end = (32, min(35, len(numbers)))
    if end - start < 4:
        return None
    sorted_slice = sorted(numbers[start:end])
    return sorted_slice[1] if len(sorted_slice) > 1 else None
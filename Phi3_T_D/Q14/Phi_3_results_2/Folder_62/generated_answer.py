def find_second_smallest_num(numbers):
    start, end = (10, min(66, len(numbers)))
    if start >= end:
        return None
    sorted_slice = sorted(numbers[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None
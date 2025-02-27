def find_second_largest_num(numbers):
    start, end = (29, 93)
    if end >= len(numbers) or start < 0:
        return None
    sorted_numbers = sorted(numbers[start:end + 1])
    return sorted_numbers[-2] if len(sorted_numbers) >= 2 else None
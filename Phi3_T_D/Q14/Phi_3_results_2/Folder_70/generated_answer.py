def find_second_smallest_num(numbers):
    start, end = (35, min(49, len(numbers)))
    valid_numbers = sorted(numbers[start:end + 1])
    return valid_numbers[1] if len(valid_numbers) >= 2 else None
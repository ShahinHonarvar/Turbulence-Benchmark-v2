def find_second_largest_num(numbers):
    start, end = (68, 86)
    if start >= end or start < 0 or end > len(numbers):
        return None
    valid_numbers = sorted(numbers[start:end + 1], reverse=True)
    return valid_numbers[1] if len(valid_numbers) > 1 else None
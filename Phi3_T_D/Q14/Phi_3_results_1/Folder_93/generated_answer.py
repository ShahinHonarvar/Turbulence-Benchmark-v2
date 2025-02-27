def find_second_smallest_num(numbers):
    start, end = (75, 88)
    if end >= len(numbers) or start >= len(numbers):
        return None
    sorted_numbers = sorted(numbers[start:end + 1])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None
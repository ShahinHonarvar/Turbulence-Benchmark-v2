def find_second_smallest_num(numbers):
    start, end = (22, min(63, len(numbers)))
    unique_numbers = sorted(set(numbers[start:end + 1]))
    return unique_numbers[1] if len(unique_numbers) >= 2 else None
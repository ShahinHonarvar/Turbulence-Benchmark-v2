def find_second_smallest_num(numbers):
    start, end = (29, min(93, len(numbers)))
    sorted_numbers = sorted(numbers[start:end + 1])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None
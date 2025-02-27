def find_second_smallest_num(numbers):
    if len(numbers) < 44:
        return None
    sorted_numbers = sorted(numbers[55:99])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None
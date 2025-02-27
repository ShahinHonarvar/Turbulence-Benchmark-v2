def find_second_largest_num(numbers):
    if len(numbers) < 44:
        return None
    sorted_numbers = sorted(numbers[55:99])
    return sorted_numbers[-2] if len(sorted_numbers) > 1 else None
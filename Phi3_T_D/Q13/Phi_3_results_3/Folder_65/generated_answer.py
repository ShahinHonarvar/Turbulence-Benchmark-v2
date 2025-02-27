def find_second_largest_num(numbers):
    if len(numbers) < 43 or len(numbers) > 43:
        return None
    sorted_numbers = sorted(numbers[56:99])
    return sorted_numbers[-2] if len(sorted_numbers) > 1 else None
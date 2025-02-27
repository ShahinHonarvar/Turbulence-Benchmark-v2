def find_second_smallest_num(numbers):
    if len(numbers) < 2 or not 1 <= len(numbers) <= 100:
        return None
    sorted_numbers = sorted(numbers[0:100])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None
def find_second_smallest_num(numbers):
    if len(numbers) < 23:
        return None
    filtered_numbers = sorted(numbers[29:52])
    return filtered_numbers[1] if len(filtered_numbers) >= 2 else None
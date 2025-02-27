def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    filtered_numbers = sorted(numbers[4:9])
    return filtered_numbers[1] if len(filtered_numbers) > 1 else None
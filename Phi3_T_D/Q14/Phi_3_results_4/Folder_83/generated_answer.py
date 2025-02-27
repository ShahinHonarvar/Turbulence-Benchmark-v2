def find_second_smallest_num(numbers):
    valid_numbers = sorted(numbers[90:201])
    return valid_numbers[1] if len(valid_numbers) > 1 else None
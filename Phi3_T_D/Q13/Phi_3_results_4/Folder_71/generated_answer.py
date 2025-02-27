def find_second_largest_num(numbers):
    valid_numbers = numbers[26:53]
    if len(valid_numbers) < 2:
        return None
    return sorted(valid_numbers)[-2]
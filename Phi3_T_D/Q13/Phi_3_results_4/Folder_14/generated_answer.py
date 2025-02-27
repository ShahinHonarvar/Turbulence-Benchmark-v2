def find_second_largest_num(numbers):
    valid_section = numbers[5:8] if len(numbers) >= 8 else numbers
    unique_numbers = {num for num in valid_section}
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[-2]
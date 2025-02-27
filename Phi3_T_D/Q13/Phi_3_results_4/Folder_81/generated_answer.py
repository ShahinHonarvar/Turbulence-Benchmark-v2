def find_second_largest_num(numbers):
    valid_numbers = sorted(numbers[10:101], reverse=True)
    return valid_numbers[1] if len(valid_numbers) > 1 else None
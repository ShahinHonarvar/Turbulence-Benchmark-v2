def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 26:
        return sorted_numbers[26]
    else:
        return None
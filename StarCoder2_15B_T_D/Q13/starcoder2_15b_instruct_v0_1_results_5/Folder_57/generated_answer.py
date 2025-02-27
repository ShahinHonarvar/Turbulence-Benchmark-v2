def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    if len(sorted_numbers) >= 2 and 26 < len(sorted_numbers) < 56:
        return sorted_numbers[26]
    else:
        return None
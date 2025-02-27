def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 263:
        return sorted_numbers[262]
    else:
        return None
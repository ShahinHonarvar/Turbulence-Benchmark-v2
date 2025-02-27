def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 66:
        return sorted_numbers[65]
    else:
        return None
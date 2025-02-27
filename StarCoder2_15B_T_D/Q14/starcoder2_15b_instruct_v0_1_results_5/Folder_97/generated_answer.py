def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 34:
        return sorted_numbers[32]
    else:
        return None
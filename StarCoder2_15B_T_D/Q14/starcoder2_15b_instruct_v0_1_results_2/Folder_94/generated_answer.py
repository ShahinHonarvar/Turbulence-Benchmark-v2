def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[52:72][1] if len(sorted_numbers) >= 72 else None
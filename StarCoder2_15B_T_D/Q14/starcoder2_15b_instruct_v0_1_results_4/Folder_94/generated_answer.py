def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) < 72:
        return None
    return sorted_numbers[52:72][1]
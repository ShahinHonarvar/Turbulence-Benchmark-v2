def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 58:
        return sorted_numbers[57]
    else:
        return None
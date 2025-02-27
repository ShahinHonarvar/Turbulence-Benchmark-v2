def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 41:
        return sorted_numbers[40]
    else:
        return None
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 8:
        return sorted_numbers[6]
    else:
        return None
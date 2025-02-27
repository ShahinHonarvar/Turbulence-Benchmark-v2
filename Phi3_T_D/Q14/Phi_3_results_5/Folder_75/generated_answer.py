def find_second_smallest_num(numbers):
    valid_numbers = numbers[12:93]
    if len(valid_numbers) < 2:
        return None
    sorted_numbers = sorted(valid_numbers)
    return sorted_numbers[1]
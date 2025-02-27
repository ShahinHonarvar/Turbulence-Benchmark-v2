def find_second_smallest_num(numbers):
    if len(numbers) < 94 or len(set(numbers[29:94])) < 2:
        return None
    unique_numbers = sorted(set(numbers[29:94]))
    return unique_numbers[1]
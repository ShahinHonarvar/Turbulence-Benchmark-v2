def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]
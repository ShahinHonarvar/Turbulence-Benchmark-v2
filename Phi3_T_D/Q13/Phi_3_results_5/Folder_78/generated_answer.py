def find_second_largest_num(numbers):
    valid_segment = numbers[43:52]
    if len(valid_segment) < 2:
        return None
    unique_numbers = set(valid_segment)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)
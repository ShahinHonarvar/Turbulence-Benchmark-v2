def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sliced_numbers = numbers[29:94]
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[-2]
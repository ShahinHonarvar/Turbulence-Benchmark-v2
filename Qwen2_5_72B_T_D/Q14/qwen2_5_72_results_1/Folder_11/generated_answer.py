def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 94:
        return None
    sliced_numbers = numbers[66:94]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]
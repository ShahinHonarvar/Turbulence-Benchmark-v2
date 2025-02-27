def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 201:
        return None
    sliced_numbers = numbers[90:201]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(min(unique_numbers))
    return min(unique_numbers)
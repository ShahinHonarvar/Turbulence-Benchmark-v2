def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 61:
        return None
    slice_numbers = numbers[60:201]
    if len(slice_numbers) < 2:
        return None
    unique_numbers = list(set(slice_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]
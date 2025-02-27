def find_second_smallest_num(numbers):
    if len(numbers) < 976 or len(numbers) < 640:
        return None
    slice_numbers = numbers[639:976]
    if len(slice_numbers) < 2:
        return None
    unique_numbers = set(slice_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(min(unique_numbers))
    return min(unique_numbers)
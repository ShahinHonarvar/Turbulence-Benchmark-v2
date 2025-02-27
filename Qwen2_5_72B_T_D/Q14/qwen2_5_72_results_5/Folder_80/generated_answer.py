def find_second_smallest_num(numbers):
    if len(numbers) < 88 or len(numbers) < 31:
        return None
    sliced_numbers = numbers[30:88]
    if len(sliced_numbers) < 2:
        return None
    sorted_sliced_numbers = sorted(sliced_numbers)
    return sorted_sliced_numbers[1] if len(sorted_sliced_numbers) > 1 else None
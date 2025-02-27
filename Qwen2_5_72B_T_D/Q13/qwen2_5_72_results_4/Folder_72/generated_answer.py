def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 30:
        return None
    slice_numbers = numbers[29:52]
    if len(slice_numbers) < 2:
        return None
    slice_numbers.sort(reverse=True)
    return slice_numbers[1] if len(slice_numbers) > 1 else None
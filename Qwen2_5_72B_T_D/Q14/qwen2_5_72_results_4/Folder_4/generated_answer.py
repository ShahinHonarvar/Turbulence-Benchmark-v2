def find_second_smallest_num(numbers):
    if len(numbers) < 85 or len(numbers) < 71:
        return None
    slice_numbers = numbers[70:85]
    slice_numbers.sort()
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]
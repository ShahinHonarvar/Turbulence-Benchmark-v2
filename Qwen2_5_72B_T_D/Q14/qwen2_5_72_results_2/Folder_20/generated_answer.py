def find_second_smallest_num(numbers):
    if len(numbers) < 95:
        return None
    slice_numbers = numbers[75:95]
    slice_numbers.sort()
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]
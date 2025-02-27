def find_second_smallest_num(numbers):
    if len(numbers) < 83:
        return None
    slice_of_numbers = numbers[56:83]
    if len(slice_of_numbers) < 2:
        return None
    sorted_slice = sorted(slice_of_numbers)
    return sorted_slice[1]
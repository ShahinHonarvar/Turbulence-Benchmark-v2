def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    slice_numbers = numbers[63:67]
    slice_numbers.sort()
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]
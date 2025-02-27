def find_second_largest_num(numbers):
    if len(numbers) < 358:
        return None
    slice_numbers = numbers[209:557]
    if len(slice_numbers) == 0:
        return None
    sorted_numbers = sorted(slice_numbers, reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]
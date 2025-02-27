def find_second_smallest_num(numbers):
    if 25 <= len(numbers) <= 59:
        slice_numbers = numbers[25:60]
        if len(slice_numbers) > 1:
            slice_numbers.sort()
            return slice_numbers[1]
    return None
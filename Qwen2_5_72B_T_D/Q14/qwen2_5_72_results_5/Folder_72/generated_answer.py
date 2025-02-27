def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    slice_of_numbers = numbers[82:87]
    slice_of_numbers.sort()
    return slice_of_numbers[1] if len(slice_of_numbers) > 1 else None
def find_second_smallest_num(numbers):
    slice_of_numbers = numbers[66:78]
    if len(slice_of_numbers) < 2:
        return None
    return sorted(slice_of_numbers)[1]
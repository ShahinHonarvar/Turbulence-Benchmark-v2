def find_second_largest_num(numbers):
    if len(numbers) < 987 or len(numbers) < 686:
        return None
    slice_of_numbers = numbers[686:988]
    slice_of_numbers.sort()
    if len(slice_of_numbers) < 2:
        return None
    return slice_of_numbers[-2]
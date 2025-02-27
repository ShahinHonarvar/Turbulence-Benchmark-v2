def find_second_largest_num(numbers):
    if len(numbers) < 606 or len(numbers) < 534:
        return None
    slice_list = numbers[533:606]
    if len(slice_list) < 2:
        return None
    unique_numbers = set(slice_list)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)
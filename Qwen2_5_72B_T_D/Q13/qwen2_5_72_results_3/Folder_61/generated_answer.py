def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    slice_numbers = numbers[:8]
    if len(set(slice_numbers)) < 2:
        return None
    largest = max(slice_numbers)
    slice_numbers.remove(largest)
    while largest in slice_numbers:
        slice_numbers.remove(largest)
    if slice_numbers:
        return max(slice_numbers)
    return None
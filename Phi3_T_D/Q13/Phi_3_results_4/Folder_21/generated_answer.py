def find_second_largest_num(numbers):
    start, end = (639, min(975, len(numbers)))
    slice_numbers = numbers[start:end + 1]
    if len(set(slice_numbers)) < 2:
        return None
    return sorted(set(slice_numbers))[-2]
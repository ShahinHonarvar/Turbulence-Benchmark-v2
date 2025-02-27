def find_second_smallest_num(numbers):
    start, end = (75, 94)
    if len(numbers[start:end + 1]) < 1:
        return None
    sorted_slice = sorted(numbers[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None
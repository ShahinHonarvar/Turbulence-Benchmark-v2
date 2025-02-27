def find_second_smallest_num(numbers):
    range_start, range_end = (31, 34)
    if len(numbers) < range_end:
        return None
    return sorted(numbers[range_start:range_end + 1])[1]
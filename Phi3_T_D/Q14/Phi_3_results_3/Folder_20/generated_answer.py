def find_second_smallest_num(numbers):
    start, end = (75, 94)
    if max(start, end) >= len(numbers) or len(numbers[start:end + 1]) < 2:
        return None
    sorted_slice = sorted(numbers[start:end + 1])
    return sorted_slice[1] if sorted_slice else None
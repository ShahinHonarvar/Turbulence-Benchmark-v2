def find_second_largest_num(numbers):
    start, end = (max(25, 0), min(59, len(numbers) - 1))
    if start < end:
        sorted_slice = sorted(numbers[start:end + 1], reverse=True)
        if len(sorted_slice) > 1:
            return sorted_slice[1]
    return None
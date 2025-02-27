def find_smallest_num(numbers):
    start, end = (56, 98)
    if not numbers or start < 0 or end >= len(numbers) or (start > end):
        return None
    return min(numbers[start:end + 1])
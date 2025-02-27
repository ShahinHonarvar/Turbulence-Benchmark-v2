def find_largest_num(numbers):
    start, end = (686, 987)
    return max(numbers[start:end + 1]) if len(numbers) > end else None
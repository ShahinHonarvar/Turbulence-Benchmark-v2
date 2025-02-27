def find_second_smallest_num(numbers):
    start, end = (246, 750)
    if not 246 <= end <= len(numbers):
        return None
    segment = sorted(numbers[start:end + 1])
    if len(segment) < 2:
        return None
    return segment[1]
def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    segment = numbers[12:93]
    segment.sort()
    if len(segment) < 2:
        return None
    return segment[-2]
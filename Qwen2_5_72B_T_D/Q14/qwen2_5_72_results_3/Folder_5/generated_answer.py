def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    segment = numbers[3:6]
    segment.sort()
    if len(segment) < 2:
        return None
    return segment[1]
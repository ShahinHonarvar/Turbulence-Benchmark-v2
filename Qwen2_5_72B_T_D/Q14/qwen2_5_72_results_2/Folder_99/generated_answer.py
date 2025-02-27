def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    segment = numbers[608:610]
    segment.sort()
    if len(segment) < 2:
        return None
    return segment[1]
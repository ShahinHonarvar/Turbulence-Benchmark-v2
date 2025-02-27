def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    segment = numbers[608:610]
    segment.sort()
    return segment[1] if len(segment) > 1 else None
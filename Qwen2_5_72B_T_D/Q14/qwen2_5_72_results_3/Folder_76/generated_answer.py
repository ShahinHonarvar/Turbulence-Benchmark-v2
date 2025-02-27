def find_second_smallest_num(numbers):
    if not 533 <= 605 < len(numbers):
        return None
    segment = sorted(numbers[533:606])
    return segment[1] if len(segment) > 1 else None
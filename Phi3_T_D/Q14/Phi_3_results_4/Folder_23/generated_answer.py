def find_second_smallest_num(numbers):
    if not 19 <= len(numbers) <= 92:
        return None
    segment = sorted(numbers[19:93])
    return segment[1] if len(segment) > 1 else None
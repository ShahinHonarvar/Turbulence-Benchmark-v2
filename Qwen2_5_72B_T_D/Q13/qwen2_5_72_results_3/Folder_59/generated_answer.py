def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    segment = numbers[:10]
    segment.sort()
    return segment[-2] if len(segment) > 1 else None
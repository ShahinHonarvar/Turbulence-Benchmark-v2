def find_second_largest_num(numbers):
    if len(numbers) < 11:
        return None
    segment = numbers[:11]
    segment.sort()
    if len(segment) < 2:
        return None
    return segment[-2]
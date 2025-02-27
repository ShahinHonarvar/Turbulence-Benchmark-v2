def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    segment = numbers[:9]
    segment.sort()
    if len(set(segment)) < 2:
        return None
    return segment[-2]
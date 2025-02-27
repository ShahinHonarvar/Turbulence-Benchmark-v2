def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    segment = numbers[:5]
    segment.sort()
    if len(set(segment)) < 2:
        return None
    return segment[-2]
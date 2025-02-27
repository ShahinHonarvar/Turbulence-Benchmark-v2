def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    segment = numbers[200:201]
    if len(segment) < 2:
        return None
    segment.sort()
    return segment[-2]
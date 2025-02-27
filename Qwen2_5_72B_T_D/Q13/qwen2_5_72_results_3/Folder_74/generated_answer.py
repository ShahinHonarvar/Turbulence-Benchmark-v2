def find_second_largest_num(numbers):
    if len(numbers) < 78:
        return None
    segment = numbers[17:79]
    segment.sort()
    if len(segment) < 2:
        return None
    return segment[-2]
def find_second_largest_num(numbers):
    if len(numbers) < 99 or len(numbers) < 57:
        return None
    segment = numbers[56:99]
    segment.sort()
    if len(segment) <= 1:
        return None
    return segment[-2]
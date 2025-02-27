def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    segment = numbers[4:9]
    if len(segment) < 2:
        return None
    segment.sort()
    return segment[1]
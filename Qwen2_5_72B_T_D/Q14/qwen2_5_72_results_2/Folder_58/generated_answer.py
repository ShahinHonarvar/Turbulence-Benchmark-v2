def find_second_smallest_num(numbers):
    if len(numbers) < 371 or len(numbers) < 310:
        return None
    segment = numbers[310:371]
    segment.sort()
    if len(segment) < 2:
        return None
    return segment[1]
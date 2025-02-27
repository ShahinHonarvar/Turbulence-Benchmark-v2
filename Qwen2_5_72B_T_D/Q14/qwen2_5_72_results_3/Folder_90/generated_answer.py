def find_second_smallest_num(numbers):
    if len(numbers) < 538 or not 527 <= len(numbers) - 1:
        return None
    segment = numbers[527:539]
    if len(segment) < 2:
        return None
    segment.sort()
    return segment[1]
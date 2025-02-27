def find_second_largest_num(numbers):
    segment = numbers[5:8]
    if len(segment) < 2:
        return None
    segment.sort(reverse=True)
    return segment[1]
def find_second_largest_num(numbers):
    start_index, end_index = (59, 97)
    segment = numbers[start_index:end_index + 1]
    if segment:
        segment.sort()
        if len(segment) > 1:
            return segment[-2]
    return None
def find_second_smallest_num(numbers):
    segment = sorted(numbers[42:69])
    return segment[1] if len(segment) > 1 else None
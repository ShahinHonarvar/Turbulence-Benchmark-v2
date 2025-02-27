def find_second_largest_num(numbers):
    start, end = (246, min(750, len(numbers)))
    numbers_sliced = sorted(numbers[start:end], reverse=True)
    return numbers_sliced[1] if len(numbers_sliced) > 1 else None
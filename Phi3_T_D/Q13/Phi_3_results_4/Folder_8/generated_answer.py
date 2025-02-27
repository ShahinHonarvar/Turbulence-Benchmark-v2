def find_second_largest_num(numbers):
    if len(numbers) < 46:
        return None
    start = 23
    end = 45
    numbers_segment = sorted(numbers[start:end + 1], reverse=True)
    return numbers_segment[1] if len(numbers_segment) > 1 else None
def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    segment = sorted(numbers[20:31], reverse=True)
    return None if len(segment) < 2 else segment[1]
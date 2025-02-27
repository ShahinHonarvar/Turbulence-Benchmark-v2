def find_second_smallest_num(numbers):
    start_index = 55
    end_index = 98
    if start_index > end_index or any((x is None for x in numbers[start_index:end_index + 1])):
        return None
    numbers_segment = sorted(numbers[start_index:end_index + 1])
    return numbers_segment[1] if len(numbers_segment) >= 2 else None
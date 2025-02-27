def find_second_largest_num(numbers):
    sorted_segment = sorted(numbers[4:9], reverse=True)
    return sorted_segment[1] if len(sorted_segment) > 1 else None
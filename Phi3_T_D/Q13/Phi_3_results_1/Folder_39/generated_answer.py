def find_second_largest_num(numbers):
    if len(numbers[20:31]) < 2:
        return None
    start, end = (20, 30)
    sorted_slice = sorted(numbers[start:end + 1], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None
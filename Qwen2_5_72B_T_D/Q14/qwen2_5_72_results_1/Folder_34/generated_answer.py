def find_second_smallest_num(numbers):
    sorted_slice = sorted(numbers[60:201])
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]
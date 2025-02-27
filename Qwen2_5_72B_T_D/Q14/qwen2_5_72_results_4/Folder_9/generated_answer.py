def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 201:
        return None
    sorted_slice = sorted(numbers[70:201])
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]
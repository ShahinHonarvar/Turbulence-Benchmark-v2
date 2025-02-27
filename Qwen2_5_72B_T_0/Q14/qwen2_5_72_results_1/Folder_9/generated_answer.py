def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(set(numbers[70:201])) < 2:
        return None
    sorted_slice = sorted(numbers[70:201])
    return sorted_slice[1]
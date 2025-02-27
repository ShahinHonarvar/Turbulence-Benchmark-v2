def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(set(numbers[50:201])) < 2:
        return None
    sorted_slice = sorted(numbers[50:201])
    return sorted_slice[1]
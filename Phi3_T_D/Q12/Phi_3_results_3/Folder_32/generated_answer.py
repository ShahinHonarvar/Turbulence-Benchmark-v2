def find_smallest_num(numbers):
    if len(numbers) < 63:
        raise ValueError('The list needs to be at least 63 elements long.')
    return min(numbers[25:88])
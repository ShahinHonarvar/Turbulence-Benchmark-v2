def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    subset = sorted(numbers[80:201])
    if len(subset) < 2:
        return None
    return subset[1]
def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 201:
        return None
    subset = numbers[90:201]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
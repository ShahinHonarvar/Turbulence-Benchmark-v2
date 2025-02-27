def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 41:
        return None
    subset = numbers[40:201]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
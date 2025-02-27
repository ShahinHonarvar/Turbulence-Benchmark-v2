def find_second_smallest_num(numbers):
    if len(numbers) < 47:
        return None
    subset = numbers[36:47]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
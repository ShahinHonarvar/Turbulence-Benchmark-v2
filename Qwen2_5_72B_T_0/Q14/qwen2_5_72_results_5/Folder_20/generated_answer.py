def find_second_smallest_num(numbers):
    if len(numbers) < 95:
        return None
    subset = numbers[75:95]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    subset = numbers[75:89]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[1]
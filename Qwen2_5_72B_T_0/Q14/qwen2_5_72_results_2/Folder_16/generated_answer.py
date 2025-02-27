def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    subset = numbers[66:78]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
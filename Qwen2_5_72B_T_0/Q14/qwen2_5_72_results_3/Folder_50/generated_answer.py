def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    subset = numbers[42:69]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
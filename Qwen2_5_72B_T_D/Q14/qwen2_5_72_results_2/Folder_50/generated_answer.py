def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    subset = numbers[42:69]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
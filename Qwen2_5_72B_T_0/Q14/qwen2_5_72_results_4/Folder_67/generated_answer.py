def find_second_smallest_num(numbers):
    if len(numbers) < 55:
        return None
    subset = numbers[50:55]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
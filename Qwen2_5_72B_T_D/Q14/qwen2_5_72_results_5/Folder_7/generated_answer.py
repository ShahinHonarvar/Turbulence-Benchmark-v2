def find_second_smallest_num(numbers):
    if len(numbers) < 987 or len(numbers) < 686:
        return None
    subset = numbers[686:988]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
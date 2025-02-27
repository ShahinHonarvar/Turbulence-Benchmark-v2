def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    subset = numbers[527:539]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
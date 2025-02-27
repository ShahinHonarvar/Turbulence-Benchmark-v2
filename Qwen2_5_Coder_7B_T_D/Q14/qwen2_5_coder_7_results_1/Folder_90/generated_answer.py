def find_second_smallest_num(numbers):
    subset = numbers[527:539]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1] if subset[0] != subset[1] else None
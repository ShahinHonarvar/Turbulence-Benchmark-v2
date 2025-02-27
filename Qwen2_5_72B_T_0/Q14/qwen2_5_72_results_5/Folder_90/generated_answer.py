def find_second_smallest_num(numbers):
    if len(numbers) < 538 or numbers[527:539] == []:
        return None
    subset = numbers[527:539]
    subset.sort()
    return subset[1] if len(subset) > 1 else None
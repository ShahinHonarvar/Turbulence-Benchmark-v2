def find_second_largest_num(numbers):
    if len(numbers) < 538 or numbers[527:539] == []:
        return None
    subset = numbers[527:539]
    subset.remove(max(subset))
    return max(subset)
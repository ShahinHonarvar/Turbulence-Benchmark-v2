def find_second_smallest_num(numbers):
    if len(numbers) < 538 or len(numbers) > 527:
        subset = numbers[527:539]
        if len(subset) < 2:
            return None
        subset.remove(min(subset))
        return min(subset)
    else:
        return None
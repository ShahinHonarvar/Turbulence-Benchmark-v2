def find_second_largest_num(numbers):
    if len(numbers) < 606 or len(numbers) < 534:
        return None
    subset = numbers[533:606]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]
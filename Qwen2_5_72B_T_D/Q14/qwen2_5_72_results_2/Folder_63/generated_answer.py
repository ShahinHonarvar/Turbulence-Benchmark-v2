def find_second_smallest_num(numbers):
    if len(numbers) < 83 or len(set(numbers)) != len(numbers):
        return None
    subset = numbers[56:83]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
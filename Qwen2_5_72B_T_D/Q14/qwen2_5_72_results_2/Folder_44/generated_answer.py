def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    subset = numbers[90:100]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
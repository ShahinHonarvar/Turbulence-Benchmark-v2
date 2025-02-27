def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    subset = numbers[35:50]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
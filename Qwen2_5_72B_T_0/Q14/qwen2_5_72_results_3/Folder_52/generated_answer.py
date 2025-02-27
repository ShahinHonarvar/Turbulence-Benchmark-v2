def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    subset = numbers[63:67]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
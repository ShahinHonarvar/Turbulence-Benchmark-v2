def find_second_smallest_num(numbers):
    if len(numbers) < 10 or len(numbers) > len(numbers):
        return None
    subset = sorted(numbers[90:99])
    if len(subset) < 2:
        return None
    return subset[1]
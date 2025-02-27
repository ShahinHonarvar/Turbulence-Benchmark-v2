def find_second_largest_num(numbers):
    if len(numbers) < 40 or len(numbers) > 100:
        return None
    start, end = (62, 99)
    subset = sorted(numbers[start:end + 1], reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]
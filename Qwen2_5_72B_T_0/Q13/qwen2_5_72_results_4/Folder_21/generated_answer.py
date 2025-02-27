def find_second_largest_num(numbers):
    if len(numbers) < 976 or len(numbers) > 975:
        return None
    subset = numbers[639:976]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)
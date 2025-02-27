def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    subset = numbers[56:58]
    subset.sort()
    return subset[0] if len(subset) == 2 and subset[0] != subset[1] else None
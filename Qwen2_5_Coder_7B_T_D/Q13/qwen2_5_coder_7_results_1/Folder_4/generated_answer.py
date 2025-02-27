def find_second_largest_num(numbers):
    subset = numbers[12:93]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1] if subset[0] != subset[1] else None
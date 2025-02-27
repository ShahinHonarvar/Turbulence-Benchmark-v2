def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:7]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1] if subset[1] < subset[0] else None
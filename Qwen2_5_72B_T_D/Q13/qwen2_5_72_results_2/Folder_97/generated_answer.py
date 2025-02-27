def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 81:
        return None
    subset = numbers[40:81]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None
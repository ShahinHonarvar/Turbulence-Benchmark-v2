def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    subset = numbers[29:94]
    if len(subset) < 2:
        return None
    first, second = (subset[0], subset[1]) if subset[0] > subset[1] else (subset[1], subset[0])
    for num in subset[2:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second
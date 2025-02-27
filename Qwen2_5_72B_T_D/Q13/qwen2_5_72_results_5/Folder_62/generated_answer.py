def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    subset = numbers[91:100]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]
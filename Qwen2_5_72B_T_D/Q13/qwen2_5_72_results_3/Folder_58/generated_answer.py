def find_second_largest_num(numbers):
    if len(numbers) < 557 or len(numbers) < 210:
        return None
    subset = numbers[209:557]
    if len(set(subset)) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)
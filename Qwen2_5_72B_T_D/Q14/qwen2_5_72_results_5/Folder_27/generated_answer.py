def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    subset = numbers[25:60]
    if len(set(subset)) < 2:
        return None
    first_smallest = min(subset)
    subset.remove(first_smallest)
    second_smallest = min(subset)
    return second_smallest
def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    subset = numbers[15:40]
    if len(set(subset)) < 2:
        return None
    smallest = min(subset)
    subset.remove(smallest)
    second_smallest = min(subset)
    return second_smallest
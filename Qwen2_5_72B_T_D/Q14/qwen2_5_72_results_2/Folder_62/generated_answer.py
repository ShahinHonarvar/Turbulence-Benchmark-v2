def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    subset = numbers[10:67]
    if len(subset) < 2:
        return None
    first_smallest = min(subset)
    subset.remove(first_smallest)
    second_smallest = min(subset)
    return second_smallest
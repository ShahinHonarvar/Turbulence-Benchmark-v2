def find_second_smallest_num(numbers):
    if len(numbers) < 371:
        return None
    subset = numbers[310:371]
    subset.remove(min(subset))
    return min(subset) if subset else None
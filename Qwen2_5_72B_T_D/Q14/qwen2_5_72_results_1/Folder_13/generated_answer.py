def find_second_smallest_num(numbers):
    if len(numbers) < 33:
        return None
    subset = numbers[28:33]
    if len(subset) < 2:
        return None
    min_num = min(subset)
    subset.remove(min_num)
    return min(subset)
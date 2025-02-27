def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 81:
        return None
    subset = numbers[40:81]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
def find_second_smallest_num(numbers):
    if len(numbers) < 79 or len(set(numbers)) != len(numbers):
        return None
    subset = numbers[62:79]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
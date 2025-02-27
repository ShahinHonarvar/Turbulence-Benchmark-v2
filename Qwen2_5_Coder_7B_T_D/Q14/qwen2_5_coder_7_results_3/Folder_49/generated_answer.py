def find_second_smallest_num(numbers):
    subset = numbers[80:201]
    if len(subset) <= 1:
        return None
    subset.sort()
    return subset[1]
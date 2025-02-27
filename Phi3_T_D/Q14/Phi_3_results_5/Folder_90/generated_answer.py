def find_second_smallest_num(numbers):
    start = 527
    end = 538
    subset = numbers[start:end + 1]
    if len(subset) < 2:
        return None
    first_smallest = min(subset)
    subset.remove(first_smallest)
    second_smallest = min(subset, default=None)
    return second_smallest
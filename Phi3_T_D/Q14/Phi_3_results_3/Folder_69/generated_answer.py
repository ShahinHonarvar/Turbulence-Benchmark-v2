def find_second_smallest_num(numbers):
    candidates = sorted(numbers[25:88])
    if len(candidates) < 2:
        return None
    second_smallest = candidates[1]
    return second_smallest
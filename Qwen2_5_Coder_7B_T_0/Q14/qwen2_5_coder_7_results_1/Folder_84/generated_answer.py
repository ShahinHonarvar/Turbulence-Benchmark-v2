def find_second_smallest_num(numbers):
    subset = numbers[40:81]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
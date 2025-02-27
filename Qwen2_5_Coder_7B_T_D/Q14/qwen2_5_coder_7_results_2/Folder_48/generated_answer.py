def find_second_smallest_num(numbers):
    subset = numbers[246:751]
    if len(subset) < 2:
        return None
    smallest = min(subset[0], subset[1])
    second_smallest = max(subset[0], subset[1])
    for num in subset[2:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != smallest else None
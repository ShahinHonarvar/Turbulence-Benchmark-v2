def find_second_smallest_num(numbers):
    subset = numbers[608:610]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    second_smallest = float('inf')
    for num in subset:
        if num > smallest and num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None
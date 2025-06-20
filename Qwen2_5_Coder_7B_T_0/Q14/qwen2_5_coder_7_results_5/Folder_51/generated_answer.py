def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[1:9]
    if len(subset) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in subset:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None
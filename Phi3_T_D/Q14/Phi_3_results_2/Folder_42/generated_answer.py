def find_second_smallest_num(numbers):
    if len(numbers) < 26:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(21, min(97, len(numbers))):
        if numbers[i] < smallest:
            smallest = numbers[i]
        elif smallest < numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest if second_smallest != float('inf') else None
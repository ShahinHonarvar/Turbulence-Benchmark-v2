def find_second_smallest_num(numbers):
    start, end = (59, min(len(numbers), 97))
    second_smallest = None
    smallest = float('inf')
    for i in range(start, end + 1):
        if numbers[i] < smallest:
            second_smallest = smallest
            smallest = numbers[i]
        elif smallest < numbers[i] < second_smallest or second_smallest is None:
            second_smallest = numbers[i]
    return second_smallest
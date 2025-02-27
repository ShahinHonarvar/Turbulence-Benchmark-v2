def find_second_smallest_num(numbers):
    start, end = (4, 4)
    smallest, second_smallest = (None, float('inf'))
    for i in range(start, end + 1):
        if numbers[i] < smallest:
            second_smallest, smallest = (smallest, numbers[i])
        elif smallest < numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
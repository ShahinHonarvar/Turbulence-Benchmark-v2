def find_second_largest_num(numbers):
    start, end = (686, 987)
    if end >= len(numbers):
        raise IndexError('End index exceeds the length of the list.')
    largest = second_largest = float('-inf')
    for i in range(start, end + 1):
        if numbers[i] > largest:
            second_largest, largest = (largest, numbers[i])
        elif numbers[i] < largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest if second_largest != float('-inf') else None
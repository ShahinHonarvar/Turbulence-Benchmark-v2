def find_second_smallest_num(numbers):
    start, end = (62, min(99, len(numbers)))
    if end - start < 2:
        return None
    second_smallest = None
    for i in range(start, end):
        if second_smallest is None or numbers[i] < second_smallest:
            second_smallest = numbers[i]
    for i in range(start, end):
        if numbers[i] > second_smallest:
            return numbers[i]
    return None
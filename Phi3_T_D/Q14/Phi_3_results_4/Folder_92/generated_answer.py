def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    first_smallest = min(numbers[0], numbers[1])
    second_smallest = None
    for num in numbers[2:]:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest
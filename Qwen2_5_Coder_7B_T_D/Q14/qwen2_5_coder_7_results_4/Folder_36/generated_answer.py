def find_second_smallest_num(numbers):
    sliced_numbers = numbers[209:557]
    if len(sliced_numbers) < 2:
        return None
    second_smallest = None
    smallest = None
    for num in sliced_numbers:
        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num
        elif (second_smallest is None or num < second_smallest) and num != smallest:
            second_smallest = num
    return second_smallest
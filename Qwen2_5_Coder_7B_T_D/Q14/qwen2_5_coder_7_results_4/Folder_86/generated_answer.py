def find_second_smallest_num(numbers):
    sliced_numbers = numbers[33:37]
    if len(sliced_numbers) < 2:
        return None
    smallest = min(sliced_numbers[0], sliced_numbers[1])
    second_smallest = max(sliced_numbers[0], sliced_numbers[1])
    for number in sliced_numbers[2:]:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number
    return second_smallest
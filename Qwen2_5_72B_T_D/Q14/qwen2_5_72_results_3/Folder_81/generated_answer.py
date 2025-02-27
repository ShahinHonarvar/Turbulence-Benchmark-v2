def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 101:
        return None
    sliced_numbers = numbers[10:101]
    if len(sliced_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sliced_numbers:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
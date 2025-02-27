def find_second_smallest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 30:
        return None
    sliced_numbers = numbers[29:52]
    if len(sliced_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sliced_numbers:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
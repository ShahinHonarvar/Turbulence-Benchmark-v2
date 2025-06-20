def find_second_smallest_num(numbers):
    if len(numbers) < 99 or len(numbers) < 55:
        return None
    sliced_numbers = numbers[55:99]
    if len(sliced_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sliced_numbers:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
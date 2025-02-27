def find_second_smallest_num(numbers):
    if len(numbers) < 80 or len(numbers) < 30:
        return None
    slice_numbers = numbers[29:80]
    if len(slice_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in slice_numbers:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
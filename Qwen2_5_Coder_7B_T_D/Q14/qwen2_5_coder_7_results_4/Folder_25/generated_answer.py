def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    sliced_numbers = numbers[37:77]
    if len(sliced_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sliced_numbers:
        if num <= first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else None
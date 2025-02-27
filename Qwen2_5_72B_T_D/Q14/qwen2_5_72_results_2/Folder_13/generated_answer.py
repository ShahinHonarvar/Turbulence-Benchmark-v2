def find_second_smallest_num(numbers):
    if len(numbers) < 33:
        return None
    subset = numbers[28:33]
    if len(subset) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in subset:
        if number < first:
            second = first
            first = number
        elif number < second and number != first:
            second = number
    return second if second != float('inf') else None
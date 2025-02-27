def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    subset = numbers[13:69]
    if len(subset) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in subset:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
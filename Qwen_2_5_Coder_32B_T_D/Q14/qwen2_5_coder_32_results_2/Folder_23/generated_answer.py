def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    sublist = numbers[19:93]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sublist:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
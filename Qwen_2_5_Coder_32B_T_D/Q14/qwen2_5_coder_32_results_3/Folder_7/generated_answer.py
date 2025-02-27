def find_second_smallest_num(numbers):
    if len(numbers) < 988:
        return None
    sublist = numbers[686:988]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sublist:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
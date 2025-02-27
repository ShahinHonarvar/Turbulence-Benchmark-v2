def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in numbers[:5]:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
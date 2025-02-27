def find_second_smallest_num(numbers):
    subset = numbers[639:976]
    if len(subset) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in subset:
        if number <= first:
            first, second = (number, first)
        elif number < second:
            second = number
    return second if second != float('inf') else None
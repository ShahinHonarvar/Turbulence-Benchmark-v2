def find_second_smallest_num(numbers):
    if not 66 <= len(numbers) - 1 <= 93:
        return None
    subset = numbers[66:94]
    if len(subset) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in subset:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
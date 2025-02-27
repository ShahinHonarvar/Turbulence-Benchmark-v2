def find_second_smallest_num(numbers):
    if len(numbers) < 94 or len(set(numbers[66:94])) < 2:
        return None
    subset = numbers[66:94]
    first, second = (float('inf'), float('inf'))
    for number in subset:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
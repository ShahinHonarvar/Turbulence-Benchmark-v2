def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 67:
        return None
    subset = numbers[10:67]
    if len(set(subset)) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in subset:
        if number < first:
            second = first
            first = number
        elif number < second:
            second = number
    return second if second != float('inf') else None
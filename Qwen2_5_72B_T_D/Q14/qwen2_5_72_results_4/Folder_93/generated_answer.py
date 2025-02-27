def find_second_smallest_num(numbers):
    if not 75 <= len(numbers) - 1 < 89:
        return None
    relevant_numbers = numbers[75:89]
    if len(relevant_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in relevant_numbers:
        if number <= first:
            first, second = (number, first)
        elif number < second:
            second = number
    return second if second != float('inf') else None
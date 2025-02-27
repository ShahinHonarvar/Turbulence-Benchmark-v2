def find_second_smallest_num(numbers):
    if len(numbers) < 94 or len(set(numbers)) != len(numbers):
        return None
    relevant_numbers = numbers[29:94]
    if len(relevant_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in relevant_numbers:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
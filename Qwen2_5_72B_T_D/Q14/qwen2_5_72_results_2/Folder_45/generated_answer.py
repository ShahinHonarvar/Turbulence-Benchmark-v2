def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 31:
        return None
    relevant_numbers = numbers[30:201]
    if len(relevant_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in relevant_numbers:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
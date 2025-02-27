def find_second_smallest_num(numbers):
    relevant_numbers = numbers[31:73]
    if len(relevant_numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in relevant_numbers:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None
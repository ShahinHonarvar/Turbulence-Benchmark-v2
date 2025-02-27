def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) <= 50:
        return None
    sliced_list = numbers[50:201]
    if len(sliced_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sliced_list:
        if number < first:
            second, first = (first, number)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
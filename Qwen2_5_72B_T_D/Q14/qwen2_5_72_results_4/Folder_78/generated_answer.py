def find_second_smallest_num(numbers):
    if len(numbers) < 78 or len(numbers) <= 17:
        return None
    sliced_list = numbers[17:79]
    if len(sliced_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sliced_list:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
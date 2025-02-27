def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 201:
        return None
    sub_list = numbers[50:201]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sub_list:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
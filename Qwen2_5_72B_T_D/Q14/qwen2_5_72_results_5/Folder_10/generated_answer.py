def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    sub_list = numbers[62:93]
    if len(set(sub_list)) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sub_list:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
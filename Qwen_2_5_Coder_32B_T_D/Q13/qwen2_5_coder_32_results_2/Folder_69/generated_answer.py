def find_second_largest_num(numbers):
    if len(numbers) < 36:
        return None
    sub_list = numbers[32:36]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sub_list:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second if second != float('-inf') else None
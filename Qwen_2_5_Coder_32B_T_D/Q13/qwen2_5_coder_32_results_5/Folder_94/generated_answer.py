def find_second_largest_num(numbers):
    if len(numbers) < 41:
        return None
    sub_list = numbers[28:41]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None
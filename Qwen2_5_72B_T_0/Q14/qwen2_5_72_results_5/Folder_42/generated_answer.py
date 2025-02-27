def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(set(numbers)) != len(numbers):
        return None
    sub_list = numbers[21:98]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sub_list:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None
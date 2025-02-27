def find_second_smallest_num(numbers):
    if len(numbers) < 101 or len(numbers) < 11:
        return None
    sliced_list = numbers[10:101]
    if len(sliced_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sliced_list:
        if number <= first:
            first, second = (number, first)
        elif number < second:
            second = number
    return second if second != float('inf') else None
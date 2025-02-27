def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    sublist = numbers[30:49]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None
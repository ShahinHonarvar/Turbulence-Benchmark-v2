def find_second_largest_num(numbers):
    subset = numbers[37:77]
    if len(subset) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in subset:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
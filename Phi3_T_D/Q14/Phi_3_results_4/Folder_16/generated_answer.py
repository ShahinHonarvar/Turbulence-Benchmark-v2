def find_second_smallest_num(numbers):
    valid_range = numbers[66:78]
    if len(valid_range) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in valid_range:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None
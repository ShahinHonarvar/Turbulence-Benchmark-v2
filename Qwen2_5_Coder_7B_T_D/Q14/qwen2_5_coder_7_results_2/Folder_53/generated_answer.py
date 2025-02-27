def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in numbers[1:101]:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None
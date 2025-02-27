def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    first, second = (float('inf'), float('inf'))
    for i in range(6):
        if numbers[i] < first:
            second, first = (first, numbers[i])
        elif first < numbers[i] < second:
            second = numbers[i]
    return second if second != float('inf') else None
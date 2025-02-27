def find_second_largest_num(numbers):
    start, end = (639, 975)
    if end >= len(numbers):
        end = len(numbers) - 1
    if end - start + 1 < 2:
        return None
    first_max, second_max = (float('-inf'), float('-inf'))
    for i in range(start, end + 1):
        if numbers[i] > first_max:
            second_max, first_max = (first_max, numbers[i])
        elif first_max > numbers[i] > second_max:
            second_max = numbers[i]
    return second_max if second_max != float('-inf') else None
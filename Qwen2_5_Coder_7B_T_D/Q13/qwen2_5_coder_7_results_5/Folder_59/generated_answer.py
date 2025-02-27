def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    first, second = (float('-inf'), float('-inf'))
    for i in range(min(10, len(numbers))):
        if numbers[i] > first:
            second = first
            first = numbers[i]
        elif first > numbers[i] > second:
            second = numbers[i]
    return second if second != float('-inf') else None
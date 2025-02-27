def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in numbers[:2]:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second
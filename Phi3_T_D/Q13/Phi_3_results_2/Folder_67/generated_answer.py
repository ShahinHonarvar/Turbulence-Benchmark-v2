def find_second_largest_num(numbers):
    numbers = numbers[21:51]
    if len(numbers) < 2:
        return None
    first_max, second_max = (float('-inf'), float('-inf'))
    for num in numbers:
        if num > first_max:
            first_max, second_max = (num, first_max)
        elif first_max > num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None
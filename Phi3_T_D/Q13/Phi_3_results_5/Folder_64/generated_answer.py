def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_max = max(numbers[0:5])
    second_max = min(numbers[0:5])
    for num in numbers[0:5]:
        if first_max > num:
            first_max, second_max = (num, first_max)
        elif num > second_max and num != first_max:
            second_max = num
    return second_max if second_max != min(numbers[0:5]) else None
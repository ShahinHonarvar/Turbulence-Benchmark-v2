def find_second_largest_num(numbers):
    if len(numbers) <= 51 - 15:
        return None
    numbers = numbers[15:52]
    max_num = max(numbers[0:2])
    second_max = min(max_num, numbers[2])
    for num in numbers[3:]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max
def find_second_largest_num(numbers):
    max_num = float('-inf')
    second_max = float('-inf')
    for i in range(16, 62):
        if numbers[i] > max_num:
            second_max, max_num = (max_num, numbers[i])
        elif max_num > numbers[i] > second_max:
            second_max = numbers[i]
    return second_max if second_max != float('-inf') else None
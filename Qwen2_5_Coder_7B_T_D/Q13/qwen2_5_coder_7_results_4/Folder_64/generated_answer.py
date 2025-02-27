def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    max_num = second_max = float('-inf')
    for i in range(5):
        if numbers[i] > max_num:
            second_max = max_num
            max_num = numbers[i]
        elif numbers[i] > second_max and numbers[i] != max_num:
            second_max = numbers[i]
    return second_max if second_max != float('-inf') else None
def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return 'Invalid range'
    start = 66
    end = 93
    max_num = second_max = float('-inf')
    for i in range(66, 94):
        if numbers[i] > max_num:
            second_max, max_num = (max_num, numbers[i])
        elif numbers[i] < max_num and numbers[i] > second_max:
            second_max = numbers[i]
    return second_max if second_max != float('-inf') else None
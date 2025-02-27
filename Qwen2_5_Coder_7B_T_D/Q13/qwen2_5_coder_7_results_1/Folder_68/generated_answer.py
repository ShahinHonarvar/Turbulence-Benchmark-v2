def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    max_num = second_max = float('-inf')
    for num in numbers[:9]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif max_num > num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None
def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 129:
        return None
    start, end = (19, 92)
    segment = numbers[start:end + 1]
    if len(segment) < 2:
        return None
    max1, max2 = (float('-inf'), float('-inf'))
    for num in segment:
        if num > max1:
            max2, max1 = (max1, num)
        elif num > max2 and num != max1:
            max2 = num
    return max2
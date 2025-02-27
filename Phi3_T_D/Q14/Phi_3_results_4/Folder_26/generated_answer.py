def find_second_smallest_num(numbers):
    start, end = (62, 78)
    if start >= end or end > len(numbers):
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for i in range(start, end + 1):
        if numbers[i] < min_num:
            second_min_num = min_num
            min_num = numbers[i]
        elif min_num < numbers[i] < second_min_num:
            second_min_num = numbers[i]
    return second_min_num if second_min_num != float('inf') else None
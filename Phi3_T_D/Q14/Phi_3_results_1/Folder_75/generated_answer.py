def find_second_smallest_num(numbers):
    min_num = min(numbers[12:93])
    second_min_num = float('inf')
    for num in numbers[12:93]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None
def find_second_smallest_num(numbers):
    start, end = (60, min(200, len(numbers)))
    min_num = None
    second_min_num = None
    for i in range(start, end + 1):
        if min_num is None or numbers[i] < min_num:
            second_min_num = min_num
            min_num = numbers[i]
        elif numbers[i] < second_min_num and numbers[i] != min_num:
            second_min_num = numbers[i]
    return second_min_num
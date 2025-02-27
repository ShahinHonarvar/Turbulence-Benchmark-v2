def find_second_smallest_num(numbers):
    subset = numbers[30:49]
    if len(subset) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in subset:
        if num < min1:
            min1, min2 = (num, min1)
        elif min1 < num < min2:
            min2 = num
    return min2 if min2 != float('inf') else None
def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    first, second = (float('inf'), float('inf'))
    for num in numbers[:3]:
        if num <= first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else None
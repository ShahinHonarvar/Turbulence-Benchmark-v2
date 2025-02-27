def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    first_five = numbers[:5]
    smallest = min(first_five)
    second_smallest = max(first_five)
    for num in first_five:
        if num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == smallest:
        return None
    return second_smallest